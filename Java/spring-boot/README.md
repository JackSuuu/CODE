# Spring Boot

## Perquisite

- ✅ Java JDK 17+ (Spring Boot 3.x requires Java 17 or newer)
- ✅ Maven or Gradle (for project management)
- ✅ An IDE like IntelliJ IDEA, VS Code, or Eclipse

## Run process

1. create `pom.xlm` to store things you need to install
2. create `mkdir src/main/java/com/example/demo` for file to compile
3. create file you need such us `HelloController.java` to print "Hello World"
4. `mvn spring-boot:run` to run server, normally in port 8080
5. Then use `curl http://localhost:8080/hello` to test

### Maven Spring Boot Plugin

`mvn spring-boot:run`
