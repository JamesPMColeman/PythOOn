"""Representations contains all classes pertaining
to the visual representatio of employees"""
class DictionaryMixin:

    def to_dict(self):
        return {
            prop: self._represent(value)
            for prop, value in self.__dict__.items()
            if not self._is_internal(prop)
        }

    def _represent(self, value):
        if isinstance(value, object):
            if hasattr(value, 'to_dict'):
                return value.to_dict()
            return str(value)
        return value

    def _is_internal(self, prop):
        return prop.startswith('_')
