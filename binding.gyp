{
  "targets": [
    {
      "target_name": "obsInterface",
      "cflags!": [ "-fno-exceptions" ],
      "cflags_cc!": [ "-fno-exceptions" ],
      "sources": [ "obsInterface.cc" ],
      "include_dirs": [
        "<!@(node -p \"require('node-addon-api').include\")",
		"..\\obs-studio\\libobs"
      ],
      "defines": [ 'NAPI_DISABLE_CPP_EXCEPTIONS' ],
	  "libraries": [
        "..\\..\\obs-studio\\build64\\libobs\\RelWithDebInfo\\obs.lib"
      ]
    }
  ]
}
