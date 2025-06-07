# GraphQL schema definitions

import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from models_db import RackModel, TankModel, SubdivisionModel


class Subdivision(SQLAlchemyObjectType):
    class Meta:
        model = SubdivisionModel


class Tank(SQLAlchemyObjectType):
    class Meta:
        model = TankModel

    subdivisions = graphene.List(lambda: Subdivision)


class Rack(SQLAlchemyObjectType):
    class Meta:
        model = RackModel

    tanks = graphene.List(lambda: Tank)


class Query(graphene.ObjectType):
    racks = graphene.List(Rack)
    tank = graphene.Field(Tank, id=graphene.Int())

    def resolve_racks(self, info):
        return RackModel.query.all()

    def resolve_tank(self, info, id):
        return TankModel.query.get(id)


schema = graphene.Schema(query=Query)

