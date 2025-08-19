GIT_TAG ?= master
TAG ?= latest

.PHONY: all judge-tier1 judge-tier2 judge-tier3 judge-tiervnoj

all: judge-tier1 judge-tier2 judge-tier3 judge-tiervnoj

judge-tier1:
	docker build --build-arg TAG="${GIT_TAG}" -t YACPS/tier-1 -t YACPS/tier-1:$(TAG) tier1

judge-tier2:
	docker build --build-arg TAG="${GIT_TAG}" -t YACPS/tier-2 -t YACPS/tier-2:$(TAG) tier2

judge-tier3:
	docker build --build-arg TAG="${GIT_TAG}" -t YACPS/tier-3 -t YACPS/tier-3:$(TAG) tier3

judge-tiervnoj:
	docker build --build-arg TAG="${GIT_TAG}" -t YACPS/tier-vnoj -t YACPS/tier-vnoj:$(TAG) tiervnoj
