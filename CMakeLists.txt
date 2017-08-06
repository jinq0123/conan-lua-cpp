project(lua-cpp CXX)
cmake_minimum_required(VERSION 2.8.12)

add_definitions(-DLUA_BUILD_AS_DLL)  

file(GLOB_RECURSE LIB_SRC RELATIVE ${CMAKE_CURRENT_SOURCE_DIR} "src/*.cpp")
list(REMOVE_ITEM LIB_SRC "src/lua.cpp" "src/luac.cpp" "src/print.cpp")
add_library(lua-cpp ${LIB_SRC})
