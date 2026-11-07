class Project:
    def __init__(self, name, description, license_name, authors,
                 dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.license_name = license_name
        self.authors = authors
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _format_list(self, items):
        if len(items) == 0:
            return ["-"]
        return [f"- {item}" for item in items]

    def __str__(self):
        lines = [
            f"Name: {self.name}",
            f"Description: {self.description or '-'}",
            f"License: {self.license_name or '-'}",
            "",
            "Authors:",
            *self._format_list(self.authors),
            "",
            "Dependencies:",
            *self._format_list(self.dependencies),
            "",
            "Development dependencies:",
            *self._format_list(self.dev_dependencies),
        ]

        return "\n".join(lines)