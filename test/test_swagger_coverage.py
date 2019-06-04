import json
import unittest
import warnings

from server import server


class TestSwaggerCoverage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = server.test_client()
        cls.BANNED_RULES = ["/spec", "/apidocs", "/static"]
        cls.THRESHOLD = 100

    def test_swagger_coverage(self):
        """ The swagger coverage should be 100% """

        self.color_print("yellow", "\n##### SWAGGER COVERAGE #####")

        swagger_specs = self.retrieve_swagger_specs()
        rules = self.filter_rules(self.client.application.url_map.iter_rules())

        (covered_methods, methods_total) = self.retrieve_covered_methods_number(
            rules, swagger_specs
        )
        coverage = int(100 * covered_methods / methods_total)

        end_color = "green" if coverage == 100 else "yellow"
        self.color_print(
            end_color,
            "%s of %s routes are swagged" % (str(covered_methods), str(methods_total)),
        )

        self.assertTrue(coverage >= self.THRESHOLD)

    def retrieve_swagger_specs(self):
        """ Fetch the swagger specs """

        # suppress flasgger unclosed file warnings
        with warnings.catch_warnings():
            warnings.filterwarnings("ignore", message="unclosed file")
            response = self.client.get("application/spec")
        response_json = json.loads(response.data.decode("utf-8"))
        swagger_specs = response_json["paths"]

        return swagger_specs

    def retrieve_covered_methods_number(self, rules, swagger_specs):
        """ Return the number of covered methods and the number of methods """
        methods_total = 0
        covered_methods = 0
        for rule in rules:
            methods = self.filter_methods(rule.methods)
            parsed_rule = self.format_rule(rule)
            for method in methods:
                methods_total += 1
                try:
                    swagger_specs[parsed_rule][method.lower()]
                    covered_methods += 1
                except KeyError:
                    self.color_print(
                        "red", "Uncovered: %s of route %s" % (method, parsed_rule)
                    )
                    continue

        return (covered_methods, methods_total)

    @staticmethod
    def filter_methods(methods):
        """ Filter methods OPTIONS and HEAD """
        return [method for method in methods if method not in ["OPTIONS", "HEAD"]]

    @staticmethod
    def format_rule(rule):
        """
        Format the rule for swagger
        Replace '<' with '{' and '>' with '}'
        Remove arguments type
        """
        return (
            str(rule)
            .replace("<", "{")
            .replace(">", "}")
            .replace("string:", "")
            .replace("int:", "")
        )

    def filter_rules(self, rules):
        """ Filter rules that do not need to be documented """
        return [rule for rule in rules if not self.is_banned_rule(rule)]

    def is_banned_rule(self, rule):
        """ Check if rule should be banned """
        return any(banned_rule in str(rule) for banned_rule in self.BANNED_RULES)

    @staticmethod
    def color_print(color, message):
        """ Print message with some nice color """
        colors = {
            "green": "\033[92m",
            "yellow": "\033[93m",
            "red": "\033[91m",
            "endc": "\033[0m",
        }

        print(colors[color] + message + colors["endc"])


if __name__ == "__main__":
    unittest.main()
