cmake_minimum_required(VERSION 2.8.12)
project(JsonTest)

find_package(cJSON REQUIRED)
add_executable(json_test json_test.c)
target_link_libraries(json_test cjson::cjson)

