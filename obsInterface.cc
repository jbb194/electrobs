#include <napi.h>
#include <obs-module.h>

Napi::String StartObs(const Napi::CallbackInfo& info) {
  Napi::Env env = info.Env();
  
  obs_startup("en-US", nullptr, nullptr);
  
  return Napi::String::New(env, "world 2");
}

Napi::Object Init(Napi::Env env, Napi::Object exports) {
  exports.Set(Napi::String::New(env, "run"),
              Napi::Function::New(env, StartObs));
  return exports;
}

NODE_API_MODULE(obsInterface, Init)
