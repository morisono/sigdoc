from abc import ABC, abstractmethod

# Abstract Factory
class AbstractFactory(ABC):
    @abstractmethod
    def create_product_a(self):
        pass
    
    @abstractmethod
    def create_product_b(self):
        pass

class ConcreteFactory1(AbstractFactory):
    def create_product_a(self):
        return ConcreteProductA1()
    
    def create_product_b(self):
        return ConcreteProductB1()

class ConcreteFactory2(AbstractFactory):
    def create_product_a(self):
        return ConcreteProductA2()
    
    def create_product_b(self):
        return ConcreteProductB2()

class ConcreteProductA1:
    def __str__(self):
        return "Product A1"

class ConcreteProductA2:
    def __str__(self):
        return "Product A2"

class ConcreteProductB1:
    def __str__(self):
        return "Product B1"

class ConcreteProductB2:
    def __str__(self):
        return "Product B2"

# Adapter
class Target:
    def request(self):
        return "Target: The default target's behavior."

class Adaptee:
    def specific_request(self):
        return ".eetpadA eht fo roivaheb laicepS"

class Adapter(Target):
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def request(self):
        return f"Adapter: (TRANSLATED) {self.adaptee.specific_request()[::-1]}"

# Bridge
class Implementor:
    def operation_impl(self):
        pass

class ConcreteImplementorA(Implementor):
    def operation_impl(self):
        return "ConcreteImplementorA: Operation implementation A"

class ConcreteImplementorB(Implementor):
    def operation_impl(self):
        return "ConcreteImplementorB: Operation implementation B"

class Abstraction:
    def __init__(self, implementor):
        self.implementor = implementor

    def operation(self):
        return f"Abstraction: Base operation with:\n{self.implementor.operation_impl()}"

# Builder
class Director:
    def __init__(self, builder):
        self._builder = builder

    def construct(self):
        self._builder.build_part_a()
        self._builder.build_part_b()

class Builder:
    @abstractmethod
    def build_part_a(self):
        pass
    
    @abstractmethod
    def build_part_b(self):
        pass

class ConcreteBuilder(Builder):
    def __init__(self):
        self.product = Product()

    def build_part_a(self):
        self.product.add("Part A")

    def build_part_b(self):
        self.product.add("Part B")

class Product:
    def __init__(self):
        self.parts = []

    def add(self, part):
        self.parts.append(part)

    def list_parts(self):
        return f"Product parts: {', '.join(self.parts)}"

# Chain of Responsibility
class Handler(ABC):
    @abstractmethod
    def handle_request(self, request):
        pass

class ConcreteHandler1(Handler):
    def handle_request(self, request):
        if request == "R1":
            return "ConcreteHandler1: Handled request R1"
        else:
            return super().handle_request(request)

class ConcreteHandler2(Handler):
    def handle_request(self, request):
        if request == "R2":
            return "ConcreteHandler2: Handled request R2"
        else:
            return super().handle_request(request)

# Command
class Receiver:
    def action(self):
        return "Receiver: Execute action"

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class ConcreteCommand(Command):
    def __init__(self, receiver):
        self._receiver = receiver

    def execute(self):
        return self._receiver.action()

class Invoker:
    def __init__(self):
        self._command = None

    def set_command(self, command):
        self._command = command

    def execute_command(self):
        return self._command.execute()

# Composite
class Component(ABC):
    @abstractmethod
    def operation(self):
        pass

class Leaf(Component):
    def operation(self):
        return "Leaf: Operation"

class Composite(Component):
    def __init__(self):
        self._children = []

    def add(self, component):
        self._children.append(component)

    def remove(self, component):
        self._children.remove(component)

    def operation(self):
        results = []
        for child in self._children:
            results.append(child.operation())
        return "\n".join(results)

# Decorator
class Component:
    @abstractmethod
    def operation(self):
        pass

class ConcreteComponent(Component):
    def operation(self):
        return "ConcreteComponent: Operation"

class Decorator(Component):
    def __init__(self, component):
        self._component = component

    def operation(self):
        return f"Decorator: Operation with {self._component.operation()}"

# Facade
class Subsystem1:
    def operation1(self):
        return "Subsystem1: Operation1"

    def operation_n(self):
        return "Subsystem1: OperationN"

class Subsystem2:
    def operation1(self):
        return "Subsystem2: Operation1"

    def operation_n(self):
        return "Subsystem2: OperationN"

class Facade:
    def __init__(self, subsystem1, subsystem2):
        self._subsystem1 = subsystem1
        self._subsystem2 = subsystem2

    def operation(self):
        results = []
        results.append("Facade initializes subsystems:")
        results.append(self._subsystem1.operation1())
        results.append(self._subsystem2.operation1())
        results.append("Facade triggers subsystems:")
        results.append(self._subsystem1.operation_n())
        results.append(self._subsystem2.operation_n())
        return "\n".join(results)

# Factory Method
class Creator(ABC):
    @abstractmethod
    def factory_method(self):
        pass

    def some_operation(self):
        product = self.factory_method()
        result = f"Creator: {product.operation()}"
        return result

class ConcreteCreator1(Creator):
    def factory_method(self):
        return ConcreteProduct1()

class ConcreteCreator2(Creator):
    def factory_method(self):
        return ConcreteProduct2()

class Product(ABC):
    @abstractmethod
    def operation(self):
        pass

class ConcreteProduct1(Product):
    def operation(self):
        return "ConcreteProduct1: Operation"

class ConcreteProduct2(Product):
    def operation(self):
        return "ConcreteProduct2: Operation"

# Flyweight
class FlyweightFactory:
    def __init__(self):
        self._flyweights = {}

    def get_flyweight(self, key):
        if key not in self._flyweights:
            self._flyweights[key] = ConcreteFlyweight()
        return self._flyweights[key]

class Flyweight:
    def operation(self, extrinsic_state):
        pass

class ConcreteFlyweight(Flyweight):
    def operation(self, extrinsic_state):
        return f"ConcreteFlyweight: Operation with {extrinsic_state}"

# Interpreter
class Context:
    def __init__(self, input_data):
        self.input_data = input_data

class AbstractExpression(ABC):
    @abstractmethod
    def interpret(self, context):
        pass

class TerminalExpression(AbstractExpression):
    def interpret(self, context):
        return "TerminalExpression: Interpreted context"

class NonTerminalExpression(AbstractExpression):
    def interpret(self, context):
        return "NonTerminalExpression: Interpreted context"

# Iterator
class Iterator(ABC):
    @abstractmethod
    def first(self):
        pass
    
    @abstractmethod
    def next(self):
        pass
    
    @abstractmethod
    def is_done(self):
        pass
    
    @abstractmethod
    def current_item(self):
        pass

class ConcreteIterator(Iterator):
    def __init__(self, collection):
        self._collection = collection
        self._index = 0

    def first(self):
        return self._collection[0]

    def next(self):
        self._index += 1
        if not self.is_done():
            return self._collection[self._index]
        else:
            return None

    def is_done(self):
        return self._index >= len(self._collection)

    def current_item(self):
        return self._collection[self._index]

class Aggregate(ABC):
    @abstractmethod
    def create_iterator(self):
        pass

class ConcreteAggregate(Aggregate):
    def __init__(self):
        self._collection = []

    def add_item(self, item):
        self._collection.append(item)

    def create_iterator(self):
        return ConcreteIterator(self._collection)

# Mediator
class Mediator(ABC):
    @abstractmethod
    def notify(self, sender, event):
        pass

class ConcreteMediator(Mediator):
    def __init__(self, component1, component2):
        self._component1 = component1
        self._component2 = component2

    def notify(self, sender, event):
        if sender == self._component1:
            return f"Mediator: Reacted to event {event} from Component1"
        elif sender == self._component2:
            return f"Mediator: Reacted to event {event} from Component2"

class Component:
    def __init__(self, mediator):
        self._mediator = mediator

    def notify(self, event):
        return self._mediator.notify(self, event)

# Memento
class Originator:
    def __init__(self, state):
        self._state = state

    def create_memento(self):
        return Memento(self._state)

    def restore_from_memento(self, memento):
        self._state = memento.state

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state):
        self._state = state

class Memento:
    def __init__(self, state):
        self._state = state

    @property
    def state(self):
        return self._state

# Observer
class Subject(ABC):
    @abstractmethod
    def attach(self, observer):
        pass
    
    @abstractmethod
    def detach(self, observer):
        pass
    
    @abstractmethod
    def notify(self):
        pass

class ConcreteSubject(Subject):
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self)

class Observer(ABC):
    @abstractmethod
    def update(self, subject):
        pass

class ConcreteObserver(Observer):
    def update(self, subject):
        return f"ConcreteObserver: Received update from {subject}"

# Prototype
import copy

class Prototype(ABC):
    @abstractmethod
    def clone(self):
        pass

class ConcretePrototype(Prototype):
    def __init__(self, state):
        self._state = state

    def clone(self):
        return copy.deepcopy(self)

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state):
        self._state = state

# Proxy
class Subject(ABC):
    @abstractmethod
    def request(self):
        pass

class RealSubject(Subject):
    def request(self):
        return "RealSubject: Handling request"

class Proxy(Subject):
    def __init__(self, real_subject):
        self._real_subject = real_subject

    def request(self):
        return f"Proxy: Checking access\n{self._real_subject.request()}"

# Singleton
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

# State
class Context:
    def __init__(self, state):
        self._state = state

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state):
        self._state = state

class State(ABC):
    @abstractmethod
    def handle(self, context):
        pass

class ConcreteStateA(State):
    def handle(self, context):
        context.state = ConcreteStateB()

class ConcreteStateB(State):
    def handle(self, context):
        context.state = ConcreteStateA()

# Strategy
class Context:
    def __init__(self, strategy):
        self._strategy = strategy

    def execute_strategy(self):
        return self._strategy.algorithm()

class Strategy(ABC):
    @abstractmethod
    def algorithm(self):
        pass

class ConcreteStrategyA(Strategy):
    def algorithm(self):
        return "ConcreteStrategyA: Algorithm implementation"

class ConcreteStrategyB(Strategy):
    def algorithm(self):
        return "ConcreteStrategyB: Algorithm implementation"

# Template Method
class AbstractClass(ABC):
    def template_method(self):
        result = []
        result.append(self.base_operation1())
        result.append(self.required_operation1())
        result.append(self.base_operation2())
        result.append(self.hook1())
        if self.hook2():
            result.append(self.required_operation2())
        return "\n".join(result)

    def base_operation1(self):
        return "AbstractClass: Base operation 1"

    @abstractmethod
    def required_operation1(self):
        pass

    def base_operation2(self):
        return "AbstractClass: Base operation 2"

    def hook1(self):
        return "AbstractClass: Hook 1"

    def hook2(self):
        return True

class ConcreteClass(AbstractClass):
    def required_operation1(self):
        return "ConcreteClass: Required operation 1"

    def required_operation2(self):
        return "ConcreteClass: Required operation 2"

# Visitor
class Visitor(ABC):
    @abstractmethod
    def visit_concrete_element_a(self, element):
        pass
    
    @abstractmethod
    def visit_concrete_element_b(self, element):
        pass

class ConcreteVisitorA(Visitor):
    def visit_concrete_element_a(self, element):
        return f"ConcreteVisitorA: Visited {element}"

    def visit_concrete_element_b(self, element):
        return f"ConcreteVisitorA: Visited {element}"

class ConcreteVisitorB(Visitor):
    def visit_concrete_element_a(self, element):
        return f"ConcreteVisitorB: Visited {element}"

    def visit_concrete_element_b(self, element):
        return f"ConcreteVisitorB: Visited {element}"

class Element(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

class ConcreteElementA(Element):
    def accept(self, visitor):
        return visitor.visit_concrete_element_a(self)

class ConcreteElementB(Element):
    def accept(self, visitor):
        return visitor.visit_concrete_element_b(self)

# 以下は各デザインパターンの利用例です

# Abstract Factory
factory1 = ConcreteFactory1()
productA1 = factory1.create_product_a()
productB1 = factory1.create_product_b()
print(productA1)  # Output: Product A1
print(productB1)  # Output: Product B1

factory2 = ConcreteFactory2()
productA2 = factory2.create_product_a()
productB2 = factory2.create_product_b()
print(productA2)  # Output: Product A2
print(productB2)  # Output: Product B2

# Adapter
adaptee = Adaptee()
adapter = Adapter(adaptee)
print(adapter.request())  # Output: Adapter: (TRANSLATED) Special behavior of the adapter.

# Bridge
implementor_a = ConcreteImplementorA()
abstraction_a = Abstraction(implementor_a)
print(abstraction_a.operation())  # Output: Abstraction: Base operation with: ConcreteImplementorA: Operation implementation A

implementor_b = ConcreteImplementorB()
abstraction_b = Abstraction(implementor_b)
print(abstraction_b.operation())  # Output: Abstraction: Base operation with: ConcreteImplementorB: Operation implementation B

# Builder
builder = ConcreteBuilder()
director = Director(builder)
director.construct()
product = builder.product
print(product.list_parts())  # Output: Product parts: Part A, Part B

# Chain of Responsibility
handler1 = ConcreteHandler1()
handler2 = ConcreteHandler2()
handler1.set_successor(handler2)
print(handler1.handle_request("R1"))  # Output: ConcreteHandler1: Handled request R1
print(handler1.handle_request("R2"))  # Output: ConcreteHandler2: Handled request R2

# Command
receiver = Receiver()
command = ConcreteCommand(receiver)
invoker = Invoker()
invoker.set_command(command)
print(invoker.execute_command())  # Output: Receiver: Execute action

# Composite
leaf1 = Leaf()
leaf2 = Leaf()
composite = Composite()
composite.add(leaf1)
composite.add(leaf2)
print(composite.operation())  # Output: Leaf: Operation\nLeaf: Operation

# Decorator
component = ConcreteComponent()
decorator = Decorator(component)
print(decorator.operation())  # Output: Decorator: Operation with ConcreteComponent: Operation

# Facade
subsystem1 = Subsystem1()
subsystem2 = Subsystem2()
facade = Facade(subsystem1, subsystem2)
print(facade.operation())
'''
Output:
Facade initializes subsystems:
Subsystem1: Operation1
Subsystem2: Operation1
Facade triggers subsystems:
Subsystem1: OperationN
Subsystem2: OperationN
'''

# Factory Method
creator1 = ConcreteCreator1()
print(creator1.some_operation())  # Output: Creator: ConcreteProduct1: Operation

creator2 = ConcreteCreator2()
print(creator2.some_operation())  # Output: Creator: ConcreteProduct2: Operation

# Flyweight
factory = FlyweightFactory()
flyweight = factory.get_flyweight("key")
print(flyweight.operation("extrinsic state"))  # Output: ConcreteFlyweight: Operation with extrinsic state

# Interpreter
context = Context("input data")
terminal_expression = TerminalExpression()
non_terminal_expression = NonTerminalExpression()
print(terminal_expression.interpret(context))  # Output: TerminalExpression: Interpreted context
print(non_terminal_expression.interpret(context))  # Output: NonTerminalExpression: Interpreted context

# Iterator
aggregate = ConcreteAggregate()
aggregate.add_item("Item 1")
aggregate.add_item("Item 2")
iterator = aggregate.create_iterator()
while not iterator.is_done():
    print(iterator.current_item())
    iterator.next()
'''
Output:
Item 1
Item 2
'''

# Mediator
component1 = Component(ConcreteMediator(component1, component2))
component2 = Component(ConcreteMediator(component1, component2))
mediator = ConcreteMediator(component1, component2)
print(component1.notify("event"))  # Output: Mediator: Reacted to event event from Component1

# Memento
originator = Originator("initial state")
memento = originator.create_memento()
originator.state = "modified state"
originator.restore_from_memento(memento)
print(originator.state)  # Output: initial state

# Observer
subject = ConcreteSubject()
observer = ConcreteObserver()
subject.attach(observer)
print(observer.update(subject))  # Output: ConcreteObserver: Received update from <__main__.ConcreteSubject object at 0x7feaa97f6940>

# Prototype
prototype = ConcretePrototype("initial state")
clone = prototype.clone()
print(clone.state)  # Output: initial state

# Proxy
real_subject = RealSubject()
proxy = Proxy(real_subject)
print(proxy.request())
'''
Output:
Proxy: Checking access
RealSubject: Handling request
'''

# Singleton
singleton1 = Singleton()
singleton2 = Singleton()
print(singleton1 == singleton2)  # Output: True

# State
context = Context(ConcreteStateA())
context.state.handle(context)
print(type(context.state) == ConcreteStateB)  # Output: True

# Strategy
context = Context(ConcreteStrategyA())
print(context.execute_strategy())  # Output: ConcreteStrategyA: Algorithm implementation

context = Context(ConcreteStrategyB())
print(context.execute_strategy())  # Output: ConcreteStrategyB: Algorithm implementation

# Template Method
concrete_class = ConcreteClass()
print(concrete_class.template_method())
'''
Output:
AbstractClass: Base operation 1
ConcreteClass: Required operation 1
AbstractClass: Base operation 2
AbstractClass: Hook 1
ConcreteClass: Required operation 2
'''

# Visitor
element_a = ConcreteElementA()
element_b = ConcreteElementB()
visitor_a = ConcreteVisitorA()
visitor_b = ConcreteVisitorB()
print(element_a.accept(visitor_a))  # Output: ConcreteVisitorA: Visited ConcreteElementA
print(element_b.accept(visitor_b))  # Output: ConcreteVisitorB: Visited ConcreteElementB


