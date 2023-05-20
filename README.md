# ai-unit-test
AI powered unit testing 
This project uses GPT to add unit tests to the files existing in the repository. It currently only supports .py files.

``` bash
bash .github/run_unit_tests.sh .github/unit-test/add_unit_tests.py
```

The unit tests will be generated in the `ai-tests` folder.

### Features

* Automatically adds unit tests to your Python files.
* Uses GPT to generate unit tests that are specific to your code.

### Limitations

* Currently only supports .py files.
* The generated unit tests may not be perfect.

### Future plans

* Add support for other file types.
* Improve the quality of the generated unit tests.
* Integrate with other testing frameworks.

### Contributing

Contributions are welcome! Please feel free to open issues or pull requests.

### License

This project is licensed under the MIT License.
