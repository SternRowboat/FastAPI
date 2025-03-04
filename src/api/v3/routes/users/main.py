feat(init): Establish FastAPI project with clean architecture

- Set up modular project structure following Domain-Driven Design principles
- Implement dependency injection pattern for database connections
- Configure PostgreSQL integration with SQLAlchemy ORM
- Set up Docker containerization with multi-stage builds
- Configure Poetry for modern Python dependency management

This commit demonstrates understanding of:
- Clean Architecture principles
- Dependency Injection patterns
- Container orchestration
- Modern Python tooling

feat(users): Implement user management with RESTful principles

- Create User domain model with SQLAlchemy
- Implement CRUD operations following REST best practices
- Add input validation using Pydantic schemas
- Implement proper error handling for edge cases
- Set up route versioning (v3) for API evolution

Demonstrates:
- RESTful API design
- Data validation patterns
- Domain modeling
- API versioning strategy

feat(testing): Add testing infrastructure and CI setup

- Configure pytest for automated testing
- Set up test containers in Docker Compose
- Add integration tests for database operations
- Configure Ruff for code quality enforcement
- Add type hints for better code maintainability

Shows expertise in:
- Test-Driven Development
- CI/CD best practices
- Code quality automation
- Type safety in Python

refactor: Update SQLAlchemy to 2.0 patterns

- Migrate to modern SQLAlchemy import patterns
- Update declarative base usage
- Maintain backward compatibility
- Improve code maintainability

Demonstrates:
- Technical debt management
- Framework version management
- Backward compatibility handling
