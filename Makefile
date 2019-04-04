.PHONY: all
all: blend color transform

.PHONY: blend
blend:
	python -m sigback.blend.tests.blend

.PHONY: color
color:
	python -m sigback.processing.tests.color

.PHONY: transform
transform:
	python -m sigback.processing.tests.transform