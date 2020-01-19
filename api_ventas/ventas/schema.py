import graphene
import graphql_jwt
from graphql_jwt.decorators import login_required
from graphene.types import Scalar
from graphene_django.types import DjangoObjectType, ObjectType
from api_ventas.ventas.models import Venta


# Create a GraphQL type for the actor model
class VentaType(DjangoObjectType):
    class Meta:
        model = Venta

class Query(ObjectType):
    ventas = graphene.List(VentaType)

    def resolve_ventas(self, info, *kwargs):
        user = info.context.user
        if not user.is_authenticated:
            raise Exception('Authentication credentials were not provided')
        return Venta.objects.all()

class VentaInput(graphene.InputObjectType):
    cantidad = graphene.Int()
    producto = graphene.String()
    precio = graphene.Float()
    reposicion = graphene.Boolean()

# Create mutations for actors
class CreateVenta(graphene.Mutation):
    class Arguments:
        input = VentaInput(required=True)

    ok = graphene.Boolean()
    venta = graphene.Field(VentaType)

    @staticmethod
    @login_required
    def mutate(root, info, input=None):
        ok = True
        venta_instance = Venta(
            cantidad=input.cantidad,
            producto=input.producto,
            precio=input.precio,
            reposicion=input.reposicion
            )
        venta_instance.save()
        return CreateVenta(ok=ok, venta=venta_instance)


class UpdateVenta(graphene.Mutation):
    class Arguments:
        id = graphene.String(required=True)
        input = VentaInput()

    ok = graphene.Boolean()
    venta = graphene.Field(VentaType)

    @staticmethod
    @login_required
    def mutate(root, info, id, input=None):
        reok = False
        venta_instance = Venta.objects.get(pk=id)
        if venta_instance:
            ok = True
            venta_instance.cantidad = input.cantidad
            venta_instance.producto = input.producto
            venta_instance.precio = input.precio
            venta_instance.reposicion = input.reposicion
            venta_instance.save()
            return UpdateVenta(ok=ok, venta=venta_instance)
        return UpdateVenta(ok=ok, venta=None)

class Mutation(graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    create_venta = CreateVenta.Field()
    update_venta = UpdateVenta.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
