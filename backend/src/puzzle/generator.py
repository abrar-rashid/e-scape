import random
from abc import ABC, abstractmethod
from dataclasses import dataclass


class Metadata(ABC):

    @classmethod
    @abstractmethod
    def get_random(cls):
        pass


@dataclass
class SeedMetadata(Metadata):
    seed: int

    @classmethod
    def get_random(cls):
        return cls(random.randint(1, 1000000))


@dataclass
class NoneMetadata(Metadata):
    @classmethod
    def get_random(cls):
        return cls()


class Generator(ABC):

    def __init__(self, solution, metadata: Metadata):
        self.metadata = metadata
        self.solution = solution

    @abstractmethod
    def generate_puzzle(self):
        pass

    @classmethod
    def get_random(cls):
        rand_solution = "".join(
            [str(random.randint(0, 9)) for _ in range(6)])
        return cls(rand_solution, cls.get_metadata().get_random())

    @classmethod
    @abstractmethod
    def get_metadata(cls):
        pass
