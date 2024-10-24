```
graph TD
  actor[User] -->|Initiates Flow| flowActor[Flow Actor]
  flowActor -->|Performs Action| target[Target]
  target -->|Completes Action| flowActor
  flowActor -->|Sends Feedback| actor
```