from enum import Enum

from pydantic import BaseModel, ConfigDict
from xsdata_pydantic.fields import field


class Appearance(BaseModel):
    class Meta:
        name = "appearance"
        namespace = "http://bitbucket.org/dan2097"

    model_config = ConfigDict(defer_build=True)
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


class EntityTypeValue(Enum):
    EXACT = "exact"
    DEFINITE_REFERENCE = "definiteReference"
    CHEMICAL_CLASS = "chemicalClass"
    FRAGMENT = "fragment"
    FALSE_POSITIVE = "falsePositive"


class NameResolved(BaseModel):
    class Meta:
        name = "nameResolved"
        namespace = "http://bitbucket.org/dan2097"

    model_config = ConfigDict(defer_build=True)
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


class ParameterPropertyType(Enum):
    FREQUENCY = "Frequency"
    LENGTH = "Length"
    PRESSURE = "Pressure"
    TIME = "Time"
    TEMPERATURE = "Temperature"
    MASS = "Mass" # TODO REVIEW Added by me
    VOLUME = "Volume" # TODO REVIEW Added by me


class PropertyTypeValue(Enum):
    AMOUNT = "AMOUNT"
    EQUIVALENTS = "EQUIVALENTS"
    MASS = "MASS"
    MOLARITY = "MOLARITY"
    VOLUME = "VOLUME"
    PH = "PH"
    PERCENTYIELD = "PERCENTYIELD"
    CALCULATEDPERCENTYIELD = "CALCULATEDPERCENTYIELD"


class ReactionActionAction(Enum):
    ADD = "Add"
    APPARATUS_ACTION = "ApparatusAction"
    CONCENTRATE = "Concentrate"
    COOL = "Cool"
    DEGASS = "Degass"
    DISSOLVE = "Dissolve"
    DRY = "Dry"
    EXTRACT = "Extract"
    FILTER = "Filter"
    HEAT = "Heat"
    IRRADIATE = "Irradiate"
    MILL = "Mill"
    PARTITION = "Partition"
    PRECIPITATE = "Precipitate"
    PURIFY = "Purify"
    QUENCH = "Quench"
    RECOVER = "Recover"
    REMOVE = "Remove"
    SAMPLE = "Sample"
    STIR = "Stir"
    SYNTHESIZE = "Synthesize"
    UNKNOWN = "Unknown"
    WAIT = "Wait"
    WASH = "Wash"
    YIELD = "Yield"
    EVAPORATE = "Evaporate" # TODO REVIEW Added by me
    SEPARATE = "Separate" # TODO REVIEW Added by me


class ReactionSmiles(BaseModel):
    class Meta:
        name = "reactionSmiles"
        namespace = "http://bitbucket.org/dan2097"

    model_config = ConfigDict(defer_build=True)
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


class Source(BaseModel):
    class Meta:
        name = "source"
        namespace = "http://bitbucket.org/dan2097"

    model_config = ConfigDict(defer_build=True)
    document_id: list[str] = field(
        default_factory=list,
        metadata={
            "name": "documentId",
            "type": "Element",
        },
    )
    paragraph_num: list[str] = field(
        default_factory=list,
        metadata={
            "name": "paragraphNum",
            "type": "Element",
        },
    )
    paragraph_text: list[str] = field(
        default_factory=list,
        metadata={
            "name": "paragraphText",
            "type": "Element",
        },
    )
    heading_text: list[str] = field(
        default_factory=list,
        metadata={
            "name": "headingText",
            "type": "Element",
        },
    )


class State(BaseModel):
    class Meta:
        name = "state"
        namespace = "http://bitbucket.org/dan2097"

    model_config = ConfigDict(defer_build=True)
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


class EntityType(BaseModel):
    class Meta:
        name = "entityType"
        namespace = "http://bitbucket.org/dan2097"

    model_config = ConfigDict(defer_build=True)
    value: EntityTypeValue = field()


class ReactionActionList(BaseModel):
    class Meta:
        name = "reactionActionList"
        namespace = "http://bitbucket.org/dan2097"

    model_config = ConfigDict(defer_build=True)
    reaction_action: list["ReactionActionList.ReactionAction"] = field(
        default_factory=list,
        metadata={
            "name": "reactionAction",
            "type": "Element",
        },
    )

    class ReactionAction(BaseModel):
        model_config = ConfigDict(defer_build=True)
        phrase_text: list[str] = field(
            default_factory=list,
            metadata={
                "name": "phraseText",
                "type": "Element",
            },
        )
        bitbucket_org_dan2097_chemical: list[
            "ReactionActionList.ReactionAction.Chemical"
        ] = field(
            default_factory=list,
            metadata={
                "name": "chemical",
                "type": "Element",
            },
        )
        chemical: list[str] = field(
            default_factory=list,
            metadata={
                "type": "Element",
            },
        )
        atmosphere: list["ReactionActionList.ReactionAction.Atmosphere"] = (
            field(
                default_factory=list,
                metadata={
                    "type": "Element",
                },
            )
        )
        parameter: list["ReactionActionList.ReactionAction.Parameter"] = field(
            default_factory=list,
            metadata={
                "type": "Element",
            },
        )
        action: None | ReactionActionAction = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )

        class Chemical(BaseModel):
            model_config = ConfigDict(defer_build=True)
            ref: None | str = field(
                default=None,
                metadata={
                    "type": "Attribute",
                },
            )

        class Atmosphere(BaseModel):
            model_config = ConfigDict(defer_build=True)
            chemical: list[str] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                },
            )
            bitbucket_org_dan2097_chemical: list[
                "ReactionActionList.ReactionAction.Atmosphere.Chemical"
            ] = field(
                default_factory=list,
                metadata={
                    "name": "chemical",
                    "type": "Element",
                },
            )

            class Chemical(BaseModel):
                model_config = ConfigDict(defer_build=True)
                ref: None | str = field(
                    default=None,
                    metadata={
                        "type": "Attribute",
                    },
                )

        class Parameter(BaseModel):
            model_config = ConfigDict(defer_build=True)
            value: str = field(
                default="",
                metadata={
                    "required": True,
                },
            )
            property_type: None | ParameterPropertyType = field(
                default=None,
                metadata={
                    "name": "propertyType",
                    "type": "Attribute",
                },
            )
            normalized_value: None | str = field(
                default=None,
                metadata={
                    "name": "normalizedValue",
                    "type": "Attribute",
                },
            )


class Chemical(BaseModel):
    class Meta:
        name = "chemical"
        namespace = "http://www.xml-cml.org/schema"

    model_config = ConfigDict(defer_build=True)
    molecule: list["Chemical.Molecule"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    amount: list["Chemical.Amount"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    identifier: list["Chemical.Identifier"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    entity_type: list[EntityType] = field(
        default_factory=list,
        metadata={
            "name": "entityType",
            "type": "Element",
            "namespace": "http://bitbucket.org/dan2097",
        },
    )
    appearance: list[Appearance] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://bitbucket.org/dan2097",
        },
    )
    state: list[State] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://bitbucket.org/dan2097",
        },
    )
    role: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    count: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )

    class Molecule(BaseModel):
        model_config = ConfigDict(defer_build=True)
        name: list["Chemical.Molecule.Name"] = field(
            default_factory=list,
            metadata={
                "type": "Element",
            },
        )
        name_resolved: list[NameResolved] = field(
            default_factory=list,
            metadata={
                "name": "nameResolved",
                "type": "Element",
                "namespace": "http://bitbucket.org/dan2097",
            },
        )
        id: None | str = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )

        class Name(BaseModel):
            model_config = ConfigDict(defer_build=True)
            value: str = field(
                default="",
                metadata={
                    "required": True,
                },
            )
            dict_ref: None | str = field(
                default=None,
                metadata={
                    "name": "dictRef",
                    "type": "Attribute",
                },
            )

    class Amount(BaseModel):
        model_config = ConfigDict(defer_build=True)
        value: str = field(
            default="",
            metadata={
                "required": True,
            },
        )
        property_type: None | PropertyTypeValue = field(
            default=None,
            metadata={
                "name": "propertyType",
                "type": "Attribute",
                "namespace": "http://bitbucket.org/dan2097",
            },
        )
        normalized_value: None | str = field(
            default=None,
            metadata={
                "name": "normalizedValue",
                "type": "Attribute",
                "namespace": "http://bitbucket.org/dan2097",
            },
        )
        units: None | str = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )

    class Identifier(BaseModel):
        model_config = ConfigDict(defer_build=True)
        dict_ref: None | str = field(
            default=None,
            metadata={
                "name": "dictRef",
                "type": "Attribute",
            },
        )
        value: None | str = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )


class ReactionList(BaseModel):
    class Meta:
        name = "reactionList"
        namespace = "http://www.xml-cml.org/schema"

    model_config = ConfigDict(defer_build=True)
    reaction: list["ReactionList.Reaction"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )

    class Reaction(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="allow")
        source: list[Source] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://bitbucket.org/dan2097",
            },
        )
        reaction_smiles: list[ReactionSmiles] = field(
            default_factory=list,
            metadata={
                "name": "reactionSmiles",
                "type": "Element",
                "namespace": "http://bitbucket.org/dan2097",
            },
        )
        product_list: list["ReactionList.Reaction.ProductList"] = field(
            default_factory=list,
            metadata={
                "name": "productList",
                "type": "Element",
            },
        )
        reactant_list: list["ReactionList.Reaction.ReactantList"] = field(
            default_factory=list,
            metadata={
                "name": "reactantList",
                "type": "Element",
            },
        )
        spectator_list: list["ReactionList.Reaction.SpectatorList"] = field(
            default_factory=list,
            metadata={
                "name": "spectatorList",
                "type": "Element",
            },
        )
        reaction_action_list: list[ReactionActionList] = field(
            default_factory=list,
            metadata={
                "name": "reactionActionList",
                "type": "Element",
                "namespace": "http://bitbucket.org/dan2097",
            },
        )

        class ProductList(BaseModel):
            model_config = ConfigDict(defer_build=True)
            product: list[Chemical] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                },
            )

        class ReactantList(BaseModel):
            model_config = ConfigDict(defer_build=True)
            reactant: list[Chemical] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                },
            )

        class SpectatorList(BaseModel):
            model_config = ConfigDict(defer_build=True)
            spectator: list[Chemical] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                },
            )
