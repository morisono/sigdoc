
1. **Abstract Factory**: This pattern provides an interface for creating families of related or dependent objects without specifying their concrete classes. It is useful when the system needs to be independent of how its objects are created, composed, and represented.

2. **Adapter**: Also known as the Wrapper pattern, it allows incompatible interfaces to work together. It converts the interface of a class into another interface that a client expects.

3. **Bridge**: This pattern decouples an abstraction from its implementation so that the two can vary independently. It is often used in situations where changes in the implementation of an abstraction should not affect clients.

4. **Builder**: The Builder pattern separates the construction of a complex object from its representation, allowing the same construction process to create different representations.

5. **Chain of Responsibility**: In this pattern, a request is passed through a chain of handlers. Each handler decides either to process the request or to pass it to the next handler in the chain.

6. **Command**: This pattern encapsulates a request as an object, thereby allowing for parameterization of clients with queues, requests, and operations.

7. **Composite**: The Composite pattern composes objects into tree structures to represent part-whole hierarchies. It lets clients treat individual objects and compositions of objects uniformly.

8. **Decorator**: Decorator attaches additional responsibilities to an object dynamically. It provides a flexible alternative to subclassing for extending functionality.

9. **Facade**: Facade provides a unified interface to a set of interfaces in a subsystem. It defines a higher-level interface that makes the subsystem easier to use.

10. **Factory Method**: This pattern defines an interface for creating an object but allows subclasses to alter the type of objects that will be created.

11. **Flyweight**: This pattern minimizes memory usage and computation by sharing as much as possible with similar objects. It is useful when the application uses a large number of objects.

12. **Interpreter**: Interpreter pattern provides a way to evaluate language grammar or expressions. It is used for defining a grammar for simple languages.

13. **Iterator**: Iterator pattern provides a way to access the elements of an aggregate object sequentially without exposing its underlying representation.

14. **Mediator**: This pattern defines an object that encapsulates how a set of objects interact. It promotes loose coupling by keeping objects from referring to each other explicitly.

15. **Memento**: Memento pattern captures and externalizes an object's internal state so that the object can be restored to this state later.

16. **Observer**: Also known as the Publish-Subscribe pattern, it defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically.

17. **Prototype**: Prototype pattern creates new objects by copying an existing object, known as the prototype. It allows for the creation of new objects without specifying their concrete classes.

18. **Proxy**: Proxy pattern provides a placeholder for another object to control access to it. It is useful in scenarios where the cost of creating the object is high or when the object needs to be accessed remotely.

19. **Singleton**: This pattern ensures that a class has only one instance and provides a global point of access to that instance.

20. **State**: State pattern allows an object to alter its behavior when its internal state changes. It appears as if the object changed its class.

21. **Strategy**: Strategy pattern defines a family of algorithms, encapsulates each one, and makes them interchangeable. It allows the algorithm to vary independently from clients that use it.

22. **Template Method**: This pattern defines the skeleton of an algorithm in the superclass but lets subclasses override specific steps of the algorithm without changing its structure.

23. **Visitor**: Visitor pattern allows for adding new operations to existing object structures without modifying them. It separates algorithms from the objects on which they operate.