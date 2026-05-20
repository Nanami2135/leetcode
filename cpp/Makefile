SHELL := /bin/sh

CMAKE ?= cmake
BUILD_DIR ?= build
BUILD_TYPE ?= Debug
PROBLEM ?=
JOBS ?= $(shell nproc 2>/dev/null || sysctl -n hw.ncpu 2>/dev/null || echo 4)

PROBLEMS := $(sort $(patsubst problems/%.cpp,%,$(wildcard problems/*.cpp)))

.DEFAULT_GOAL := help
.PHONY: help configure build all run list clean distclean rebuild check-problem

help:
	@printf '%s\n' 'LeetCode C++ workspace'
	@printf '\n'
	@printf '%s\n' 'Targets:'
	@printf '  %-22s %s\n' 'make configure' 'Configure the CMake build directory'
	@printf '  %-22s %s\n' 'make build' 'Build all problem executables'
	@printf '  %-22s %s\n' 'make run PROBLEM=103' 'Build and run one problem'
	@printf '  %-22s %s\n' 'make list' 'List available problem numbers'
	@printf '  %-22s %s\n' 'make clean' 'Clean compiled outputs through CMake'
	@printf '  %-22s %s\n' 'make distclean' 'Remove the build directory'
	@printf '\n'
	@printf '%s\n' 'Variables:'
	@printf '  %-22s %s\n' 'BUILD_DIR=build' 'CMake build directory'
	@printf '  %-22s %s\n' 'BUILD_TYPE=Debug' 'CMake build type'
	@printf '  %-22s %s\n' 'JOBS=$(JOBS)' 'Parallel build jobs'

configure:
	$(CMAKE) -S . -B "$(BUILD_DIR)" -DCMAKE_BUILD_TYPE="$(BUILD_TYPE)" -DCMAKE_EXPORT_COMPILE_COMMANDS=ON

build: configure
	$(CMAKE) --build "$(BUILD_DIR)" --config "$(BUILD_TYPE)" --parallel "$(JOBS)"

all: build

run: check-problem configure
	$(CMAKE) --build "$(BUILD_DIR)" --config "$(BUILD_TYPE)" --target "$(PROBLEM)" --parallel "$(JOBS)"
	"$(BUILD_DIR)/bin/$(PROBLEM)"

list:
	@printf '%s\n' $(PROBLEMS)

clean:
	@if [ -d "$(BUILD_DIR)" ]; then \
		$(CMAKE) --build "$(BUILD_DIR)" --target clean; \
	fi

distclean:
	rm -rf "$(BUILD_DIR)"

rebuild: distclean build

check-problem:
	@if [ -z "$(PROBLEM)" ]; then \
		printf '%s\n' 'Set a problem number, for example: make run PROBLEM=103' >&2; \
		exit 2; \
	fi
	@if [ ! -f "problems/$(PROBLEM).cpp" ]; then \
		printf 'Problem %s not found at problems/%s.cpp\n' "$(PROBLEM)" "$(PROBLEM)" >&2; \
		exit 2; \
	fi
