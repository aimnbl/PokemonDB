from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from .models import Pokemon

@registry.register_document
class PokemonDocument(Document):
    class Index:
        # Name of the Elasticsearch index
        name = 'pokemons'
        # See Elasticsearch Indices API reference for available settings
        settings = {'number_of_shards': 1,
                    'number_of_replicas': 0}

    class Django:
        model = Pokemon # The model associated with this Document

        # The fields of the model you want to be indexed in Elasticsearch
        fields = [
            'name',
            'species'
        ]