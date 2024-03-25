
CONSTANCE_IGNORE_ADMIN_VERSION_CHECK = True


CONSTANCE_CONFIG = {
    'CHANGE_STATUS_IN_MIXER': ("WA", 'order status after mixer, \n PA -payment accepted / WA-Waiting for acception , OA-order accepted/, OS-order sended ', str),
    "USE_NEW_MIXER": (False, 'using new mixer', bool ),
    "AUTO_CREATE_RESULT": (False, 'order auto create result', bool),
    "MICRO_DEBUG":(False, 'micro debug function - tests', bool),
    
}

CONSTANCE_CONFIG_FIELDSETS = {
    'General options':(
        'CHANGE_STATUS_IN_MIXER',
    ),
    'Mixer':(
        'USE_NEW_MIXER',
        'AUTO_CREATE_RESULT',
    ),
    'Tests':{
        'MICRO_DEBUG',
    },
}
