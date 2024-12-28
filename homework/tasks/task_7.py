import abc
import asyncio
from concurrent.futures import ThreadPoolExecutor


class AbstractModel:
    @abc.abstractmethod
    def compute(self):
        ...


class Handler:
    def __init__(self, model: AbstractModel):
        self._model = model
        self._executor = ThreadPoolExecutor()

    async def handle_request(self) -> None:
        """
        Efficiently execute heavy computations
        """

        loop = asyncio.get_event_loop()
        await loop.run_in_executor(self._executor, self._model.compute)
