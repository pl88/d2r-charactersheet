from models.base import BaseModel
from sqlalchemy import Column, String, Integer


class Character(BaseModel):
    __tabelename__ = "characters"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    level = Column(Integer, nullable=False)
    character_class: str = Column(String(50), nullable=False)
    strength = Column(Integer, default=0)
    dexterity = Column(Integer, default=0)
    vitality = Column(Integer, default=0)
    energy = Column(Integer, default=0)
    life = Column(Integer, default=0)
    mana = Column(Integer, default=0)
    stamina = Column(Integer, default=0)
    life_per_level = Column(Integer, default=0)
    mana_per_level = Column(Integer, default=0)
    stamina_per_level = Column(Integer, default=0)
    life_per_vitality = Column(Integer, default=0)
    stamina_per_vitality = Column(Integer, default=0)
    mana_per_energy = Column(Integer, default=0)
    attribute_points = Column(Integer, default=0)
    skill_points = Column(Integer, default=0)
