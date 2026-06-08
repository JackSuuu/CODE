#include <boost/beast/core.hpp>
#include <boost/beast/http.hpp>
#include <boost/beast/version.hpp>
#include <boost/asio/ip/tcp.hpp>
#include <boost/config.hpp>
#include <cstdlib>
#include <iostream>
#include <memory>
#include <string>
#include <thread>

namespace beast = boost::beast;
namespace http = beast::http;
namespace net = boost::asio;
using tcp = boost::asio::ip::tcp;

// To compile: g++ -std=c++17 -I/opt/homebrew/include -o rest_api server.cpp -L/opt/homebrew/lib -lboost_system -lboost_thread -pthread
// Helper function to create HTTP responses
template<class Body, class Allocator>
http::response<http::string_body> create_response(
    http::request<Body, http::basic_fields<Allocator>>&& req,
    http::status status,
    std::string&& content)
{
    http::response<http::string_body> res{status, req.version()};
    res.set(http::field::server, BOOST_BEAST_VERSION_STRING);
    res.set(http::field::content_type, "application/json");
    res.body() = content;
    res.prepare_payload();
    res.keep_alive(req.keep_alive());
    return res;
}

// Handle HTTP request and produce response
void handle_request(http::request<http::string_body>&& req, tcp::socket& socket)
{
    http::response<http::string_body> res;
    
    // Handle GET request
    if(req.method() == http::verb::get) {
        if(req.target() == "/api/hello") {
            res = create_response(
                std::move(req),
                http::status::ok,
                R"({"message": "GET request received", "greeting": "Hello C++ Restful API"})");
        } else {
            res = create_response(
                std::move(req),
                http::status::not_found,
                R"({"error": "Resource not found"})");
        }
    }

    // Handle GET request
    else if(req.method() == http::verb::get) {
        if(req.target() == "/api/data") {
            res = create_response(
                std::move(req),
                http::status::ok,
                R"({"message": "GET request received", "data": []})");
        } else {
            res = create_response(
                std::move(req),
                http::status::not_found,
                R"({"error": "Resource not found"})");
        }
    }

    // Handle POST request
    else if(req.method() == http::verb::post) {
        if(req.target() == "/api/data") {
            std::cout << "Received POST data: " << req.body() << std::endl;
            res = create_response(
                std::move(req),
                http::status::created,
                R"({"message": "Data created successfully"})");
        } else {
            res = create_response(
                std::move(req),
                http::status::not_found,
                R"({"error": "Resource not found"})");
        }
    }
    else {
        res = create_response(
            std::move(req),
            http::status::bad_request,
            R"({"error": "Invalid HTTP method"})");
    }

    // Send the response
    http::write(socket, res);
}

// Accept HTTP connections
void do_session(tcp::socket& socket)
{
    try {
        beast::flat_buffer buffer;
        http::request<http::string_body> req;
        http::read(socket, buffer, req);
        handle_request(std::move(req), socket);
    }
    catch(const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
    }
}

int main()
{
    try {
        auto const address = net::ip::make_address("0.0.0.0");
        auto const port = static_cast<unsigned short>(8080);

        net::io_context ioc{1};
        tcp::acceptor acceptor{ioc, {address, port}};

        while(true) {
            tcp::socket socket{ioc};
            acceptor.accept(socket);
            do_session(socket);
        }
    }
    catch(const std::exception& e) {
        std::cerr << "Server failure: " << e.what() << std::endl;
        return 1;
    }
    return 0;
}