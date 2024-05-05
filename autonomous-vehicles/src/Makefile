.PHONY: version build run clean

version:
	@echo "Version 1.0.0"
	// Add your version commands here
	version=1.0.0
	version_file="version.txt"
	echo $$version > $$version_file
	$$version=$$(cat $$version_file)
	echo "Version: $$version"

build:
	@echo "Building the project..."
	# Add your build commands here
	cargo build --release

run: build
	@echo "Running the project..."
	# Add your run commands here
	cargo run --release

clean:
	@echo "Cleaning the project..."
	# Add your clean commands here
	cargo clean

commit:
	@echo "Updating version number..."
	# Add your commit commands here
	git add .
	git commit -m "Updated version number"
	git push -u origin main
