cmake_minimum_required (VERSION 3.1)
project (llfit)

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)
set(CMAKE_BUILD_TYPE Release)

find_package(Minuit2 REQUIRED)

include_directories(include)

file(GLOB SOURCES src/*.cpp)

add_executable(${PROJECT_NAME} ${SOURCES})
target_link_libraries(${PROJECT_NAME} PUBLIC Minuit2::Minuit2)
