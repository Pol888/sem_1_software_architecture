from abc import ABC, abstractmethod


class IModelChanger(ABC):
    @abstractmethod
    def notify_change(self, i_m_c_sender):
        pass