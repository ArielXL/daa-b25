.PHONY: clean

NAME 	   		:= Diseño de Análisis y Algoritmos
VERSION			:= 1.0
DEVELOPERS		:= Ariel Plasencia Díaz
COPYRIGHT  	    := Copyright © 2025: $(DEVELOPERS)


run: ## Run the main program
	python3 main.py

info: ## Display project description
	@echo "$(NAME) v$(VERSION)"
	@echo "$(COPYRIGHT)"

version: ## Show the project version
	@echo "$(NAME) v$(VERSION)"

remove: ## Remove generated files
	make remove-dot
	make remove-png

remove-dot: ## Remove generated DOT files
	rm -rf ../doc/50-nodos/*.dot
	rm -rf ../doc/200-nodos/*.dot
	rm -rf ../doc/500-nodos/*.dot

remove-png: ## Remove generated PNG images
	rm -rf ../doc/50-nodos/*.png
	rm -rf ../doc/200-nodos/*.png
	rm -rf ../doc/500-nodos/*.png

install: ## Install the project dependencies
	pip3 install -r ../requirements.txt

help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
