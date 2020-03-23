from absl import logging

from .codeepneat_module_base import CoDeepNEATModuleBase
from .codeepneat_module_dense_network import CoDeepNEATModuleDenseNetwork


class CoDeepNEATModuleDense(CoDeepNEATModuleBase):
    """"""

    def __init__(self,
                 module_id,
                 merge_method,
                 units,
                 activation,
                 kernel_initializer,
                 bias_initializer,
                 dropout_flag,
                 dropout_rate):
        """"""
        # Register parameters
        super().__init__(module_id, merge_method)
        self.units = units
        self.activation = activation
        self.kernel_initializer = kernel_initializer
        self.bias_initializer = bias_initializer
        self.dropout_flag = dropout_flag
        self.dropout_rate = dropout_rate

    def __str__(self) -> str:
        """"""
        logging.debug("\t\tToDo: Create string representation of CDN Dense Module")
        return "ToDo: Create string representation of CDN Dense Module"

    def create_module(self,
                      dtype,
                      output_units=None,
                      output_activation=None) -> CoDeepNEATModuleDenseNetwork:
        """"""
        network_units = self.units if output_units is None else output_units
        network_activation = self.activation if output_activation is None else output_activation
        return CoDeepNEATModuleDenseNetwork(units=network_units,
                                            activation=network_activation,
                                            kernel_initializer=self.kernel_initializer,
                                            bias_initializer=self.bias_initializer,
                                            dropout_flag=self.dropout_flag,
                                            dropout_rate=self.dropout_rate,
                                            dtype=dtype)
