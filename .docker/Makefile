GIT_TAG ?= master
TAG ?= latest
NO_CACHE ?= false  # default is false

.PHONY: all judge-tier1 judge-tier2 judge-tier3 judge-tiervnoj

# Convert NO_CACHE=true into the actual docker flag
ifeq ($(NO_CACHE),true)
	DOCKER_NO_CACHE := --no-cache
else
	DOCKER_NO_CACHE :=
endif

all: judge-tier1 judge-tier2 judge-tier3 judge-tiervnoj

define build_docker
	docker build $(DOCKER_NO_CACHE) --build-arg TAG="${GIT_TAG}" -t YACPS/$(1) -t YACPS/$(1):$(TAG) $(2)
endef

judge-tier1:
	$(call build_docker,tier-1,tier1)

judge-tier2:
	$(call build_docker,tier-2,tier2)

judge-tier3:
	$(call build_docker,tier-3,tier3)

judge-tiervnoj:
	$(call build_docker,tier-vnoj,tiervnoj)
