class ReportGenerator:
    @staticmethod
    def generate_report(sites):
        report = "Afforestation Mission Report\n"
        report += "Number of sites planted: " + str(len(sites)) + "\n"
        for site in sites:
            report += f"Site: {site}\n"
        report += "End of Report."
        return report
