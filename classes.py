# Amazon, Assassin, Barbarian, Druid, Necromancer, Paladin, Sorceress
import json
from pydantic import BaseModel, Field, ValidationError


class ClassModifier(BaseModel):
    class_name: str
    starting_strength: int = Field(default=0, ge=0)
    starting_dexterity: int = Field(default=0, ge=0)
    starting_vitality: int = Field(default=0, ge=0)
    starting_energy: int = Field(default=0, ge=0)
    starting_life: int = Field(default=0, ge=0)
    starting_mana: int = Field(default=0, ge=0)
    starting_stamina: int = Field(default=0, ge=0)
    life_per_level: float = Field(default=0, ge=0)
    mana_per_level: float = Field(default=0, ge=0)
    stamina_per_level: float = Field(default=0, ge=0)
    life_per_vitality: float = Field(default=0, ge=0)
    stamina_per_vitality: float = Field(default=0, ge=0)
    mana_per_energy: float = Field(default=0, ge=0)


with open("class_modifiers.json", "r") as f:
    class_modifiers = json.load(f)

for key, value in class_modifiers.items():
    try:
        class_modifiers[key] = ClassModifier(**value)
    except ValidationError as e:
        print(f"Error validating {key}: {e}")


class Character(BaseModel):
    name: str
    level: int = Field(default=1, ge=1)
    character_class: str
    strength: int = Field(default=0, ge=0)
    dexterity: int = Field(default=0, ge=0)
    vitality: int = Field(default=0, ge=0)
    energy: int = Field(default=0, ge=0)
    life: int = Field(default=0, ge=0)
    mana: int = Field(default=0, ge=0)
    stamina: int = Field(default=0, ge=0)

    life_per_level: float = Field(default=0, ge=0)
    mana_per_level: float = Field(default=0, ge=0)
    stamina_per_level: float = Field(default=0, ge=0)
    life_per_vitality: float = Field(default=0, ge=0)
    stamina_per_vitality: float = Field(default=0, ge=0)
    mana_per_energy: float = Field(default=0, ge=0)

    attribute_points: int = Field(default=0, ge=0)
    skill_points: int = Field(default=0, ge=0)

    def __str__(self):
        desc = f"""
                    Character: {self.name},
                    \n
                    Level: {self.level},
                    Class: {self.character_class},
                    \n
                    Strength: {self.strength},
                    Dexterity: {self.dexterity},
                    Vitality: {self.vitality},
                    Energy: {self.energy},
                    Life: {self.life},
                    Mana: {self.mana},
                    Stamina: {self.stamina}
                    \n
                    Attribute Points: {self.attribute_points},
                    Skill Points: {self.skill_points}
                """
        return desc


def create_character(name: str, character_class: ClassModifier) -> Character:
    return Character(
        name=name,
        character_class=character_class.class_name,
        strength=character_class.starting_strength,
        dexterity=character_class.starting_dexterity,
        vitality=character_class.starting_vitality,
        energy=character_class.starting_energy,
        life=character_class.starting_life,
        mana=character_class.starting_mana,
        stamina=character_class.starting_stamina,
        life_per_level=character_class.life_per_level,
        mana_per_level=character_class.mana_per_level,
        stamina_per_level=character_class.stamina_per_level,
        life_per_vitality=character_class.life_per_vitality,
        stamina_per_vitality=character_class.stamina_per_vitality,
        mana_per_energy=character_class.mana_per_energy
    )


def level_up(character: Character):
    character.level += 1
    character.attribute_points += 5
    character.skill_points += 1
    character.life += character.life_per_level
    character.mana += character.mana_per_level
    character.stamina += character.stamina_per_level


def set_level(character: Character, level: int):
    if level < character.level:
        raise ValueError("Cannot set level lower than current level.")
    for i in range(level - character.level):
        level_up(character)


def add_strength(character: Character):
    if character.attribute_points > 0:
        character.strength += 1
        character.attribute_points -= 1


def add_dexterity(character: Character):
    if character.attribute_points > 0:
        character.dexterity += 1
        character.attribute_points -= 1


def add_vitality(character: Character):
    if character.attribute_points > 0:
        character.vitality += 1
        character.life += character.life_per_vitality
        character.stamina += character.stamina_per_vitality
        character.attribute_points -= 1


def add_energy(character: Character):
    if character.attribute_points > 0:
        character.energy += 1
        character.mana += character.mana_per_energy
        character.attribute_points -= 1


def add_den_bonus(character: Character):
    character.attribute_points += 1


def add_radament_bonus(character: Character):
    character.skill_points += 1


def add_potion_bonus(character: Character):
    character.life += 20


def add_izual_bonus(character: Character):
    character.skill_points += 2


sparky = create_character("Sparky", class_modifiers["Sorceress"])
print(sparky)

set_level(sparky, 10)
print(sparky)
