project(lua-cpp CXX)
cmake_minimum_required(VERSION 2.8.12)

file(GLOB_RECURSE LIB_SRC RELATIVE ${CMAKE_CURRENT_SOURCE_DIR} "src/*.cpp")
list(REMOVE_ITEM LIB_SRC "src/lua.cpp" "src/luac.cpp")
add_library(lua-cpp SHARED ${LIB_SRC})
if(WIN32)
    set_target_properties(lua-cpp PROPERTIES COMPILE_DEFINITIONS LUA_BUILD_AS_DLL)
else()
    # To fix: dynamic libraries not enabled
    add_definitions(-DLUA_USE_LINUX)
    target_link_libraries(lua-cpp dl readline)
endif()

add_executable(lua-cpp-console "src/lua.cpp")
set_target_properties(lua-cpp-console PROPERTIES OUTPUT_NAME "lua-cpp")
target_link_libraries(lua-cpp-console lua-cpp)
add_executable(luac-cpp "src/luac.cpp" "src/ldump.cpp" "src/lopcodes.cpp")
target_link_libraries(luac-cpp lua-cpp)
