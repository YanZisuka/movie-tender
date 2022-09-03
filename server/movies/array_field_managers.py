from typing import List, Set
from abc import ABC, abstractmethod


class ArrayFieldManager(ABC):
    @property
    @abstractmethod
    def set(self) -> Set[str]:
        pass

    @abstractmethod
    def contains(self, genre: str):
        pass

    @abstractmethod
    def add(self, genre: str):
        pass

    @abstractmethod
    def remove(self, genre: str):
        pass

    @abstractmethod
    def _commit(self):
        pass


class Genres(ArrayFieldManager):
    def __init__(self, genres: List[str], movie):
        self.genres = set(genres)
        self._movie = movie

    @property
    def set(self) -> Set[str]:
        return self.genres

    def contains(self, genre: str):
        return genre in self.genres

    def add(self, genre: str):
        self.genres.add(genre)
        self._commit()

    def remove(self, genre: str):
        if not self.contains(genre):
            return
        self.genres.remove(genre)
        self._commit()

    def _commit(self):
        self._movie._genres = list(self.genres)
        self._movie.save(update_fields=["_genres"])


class Keywords(ArrayFieldManager):
    def __init__(self, keywords: List[str], movie):
        self.keywords = set(keywords)
        self._movie = movie

    @property
    def set(self) -> Set[str]:
        return self.keywords

    def contains(self, keyword: str):
        return keyword in self.keywords

    def add(self, keyword: str):
        self.keywords.add(keyword)
        self._commit()

    def remove(self, keyword: str):
        if not self.contains(keyword):
            return
        self.keywords.remove(keyword)
        self._commit()

    def _commit(self):
        self._movie._keywords = list(self.keywords)
        self._movie.save(update_fields=["_keywords"])


class Providers(ArrayFieldManager):
    def __init__(self, providers: List[str], movie):
        self.providers = set(providers)
        self._movie = movie

    @property
    def set(self) -> Set[str]:
        return self.providers

    def contains(self, provider: str):
        return provider in self.providers

    def add(self, provider: str):
        self.providers.add(provider)
        self._commit()

    def remove(self, provider: str):
        if not self.contains(provider):
            return
        self.providers.remove(provider)
        self._commit()

    def _commit(self):
        self._movie._providers = list(self.providers)
        self._movie.save(update_fields=["_providers"])
