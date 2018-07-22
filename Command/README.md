# 命令设计模式
四大参与者：
- Command
- ConcreteCommand
- Invoker
- Receiver

Receiver(接收器)负责接受参数  
Command 执行命令操作的接口  
ConcreteCommand 将Receiver与Command绑定  
Invoker 操纵ConcreteCommand执行请求  
  
降低了代码间的耦合程度，更利于程序拓展  