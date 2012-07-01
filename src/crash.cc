#include <node.h>
#include <v8.h>

using namespace v8;

Handle<Value>
Method(const Arguments& args) {
  HandleScope scope;
  delete (int*)0xffffffff;
  throw "Crash!";
  return scope.Close(String::New("Unreachable!"));
}

extern "C" void
init(Handle<Object> target) {
  target->Set(String::NewSymbol("crash"),
    FunctionTemplate::New(Method)->GetFunction());
}
NODE_MODULE(crash, init)
