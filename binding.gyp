{
  'targets': [ {
    'target_name': 'crash'
  , 'sources': [ 'src/crash.cc' ]
  , 'cflags!': [ '-fno-exceptions' ]
  , 'cflags_cc!': [ '-fno-exceptions' ]
  , 'conditions': [
      ['OS=="mac"', {
        'xcode_settings': {
          'GCC_ENABLE_CPP_EXCEPTIONS': 'NO',        # -fno-exceptions
      	}
      }]
  	]
  }]
}