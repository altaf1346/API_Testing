# API Testing Project

## Project Purpose
This project is designed to automate API testing using Python. It integrates with GitHub Actions for regression testing, ensuring the stability of APIs over time.

## Features
- Automated regression suite using `pytest`.
- Continuous Integration (CI) pipeline via GitHub Actions.
- HTML reports for test results (powered by `pytest-html`).

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/altaf1346/API_Testing.git
   cd API_Testing
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run tests locally:
   ```bash
   pytest
   ```

4. View test reports:
   - After running tests, open `report.html` in your browser to view detailed results.

## CI/CD Integration
This project uses GitHub Actions for continuous integration:
- On every push or pull request to the `main` branch, tests are executed automatically.
- Test reports are uploaded as artifacts.

## Planned Enhancements
- **Authentication Testing**: Add tests for OAuth and JWT-based APIs.
- **Error Handling Tests**: Validate response codes for various error scenarios (4xx, 5xx).
- **Performance Testing**: Integrate tools like Postman and JMeter for load and response time testing.

## Contributing
Feel free to fork the repository and raise pull requests with enhancements or bug fixes.
