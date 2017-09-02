import static spark.Spark.*;

public class HelloWorld {
    public static void main(String[] args) {
        get("/hello/:name", (request, response) -> {return "Hello: " + request.params(":name");});
	
	
    }
}
