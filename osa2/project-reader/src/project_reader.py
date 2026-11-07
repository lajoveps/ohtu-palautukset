import re
from urllib import request
import tomli
from project import Project


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def _package_name(self, requirement):
        # "flask>=3.1.3" -> "flask"
        return re.split(r"[\s<>=!~;\[(]", requirement, maxsplit=1)[0]

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")

        # deserialisoi TOML-formaatissa oleva merkkijono sanakirjaksi
        data = tomli.loads(content)
        project = data["project"]

        authors = [author["name"] for author in project.get("authors", [])]

        dependencies = [
            self._package_name(dep)
            for dep in project.get("dependencies", [])
        ]
        if "requires-python" in project:
            dependencies.insert(0, "python")

        dev_dependencies = [
            self._package_name(dep)
            for dep in data.get("dependency-groups", {}).get("dev", [])
        ]

        return Project(
            project["name"],
            project.get("description"),
            project.get("license"),
            authors,
            dependencies,
            dev_dependencies
        )