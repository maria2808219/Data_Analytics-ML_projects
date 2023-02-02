--- COUNTRIES

SELECT location
	, CONVERT(date, ISNULL(date, 0)) AS Date
	, population
	, total_cases AS TotalCases
	, 100*CONVERT(numeric, total_cases, 0)/population AS PerTotalCases
	, ISNULL(CONVERT(numeric, total_deaths, 0), 0) AS TotalDeath
	, ISNULL(100*CONVERT(numeric, total_deaths, 0)/population, 0) AS PerTotalDeath
    , ISNULL(CONVERT(numeric, people_vaccinated, 0),0) AS VaccinationFirst
	, ISNULL(CONVERT(numeric, people_fully_vaccinated, 0),0) AS VaccinationFully
	, ISNULL(CONVERT(numeric, total_boosters, 0),0) AS VaccinationBooster
	, ISNULL(100*CONVERT(numeric, people_vaccinated, 0)/population, 0) AS VaccinationPerFirst
	, ISNULL(100*CONVERT(numeric, people_fully_vaccinated, 0)/population, 0) AS VaccinationPerFully
	, ISNULL(100*CONVERT(numeric, total_boosters, 0)/population, 0) AS VaccinationPerBooster
FROM PortfolioProject..Covid
WHERE location in ('Belarus', 'Russia', 'Ukraine', 'Poland', 'Latvia', 'Lithuania')
ORDER BY location, date


--- VACCINATION WORLD


SELECT location
	, CONVERT(date, ISNULL(date, 0)) AS Date
	, population
	, total_cases AS TotalCases
	, 100*CONVERT(numeric, total_cases, 0)/population AS PerTotalCases
	, ISNULL(CONVERT(numeric, total_deaths, 0), 0) AS TotalDeath
	, ISNULL(100*CONVERT(numeric, total_deaths, 0)/population, 0) AS PerTotalDeath
    , ISNULL(CONVERT(numeric, people_vaccinated, 0),0) AS VaccinationFirst
	, ISNULL(CONVERT(numeric, people_fully_vaccinated, 0),0) AS VaccinationFully
	, ISNULL(CONVERT(numeric, total_boosters, 0),0) AS VaccinationBooster
	, ISNULL(100*CONVERT(numeric, people_vaccinated, 0)/population, 0) AS VaccinationPerFirst
	, ISNULL(100*CONVERT(numeric, people_fully_vaccinated, 0)/population, 0) AS VaccinationPerFully
	, ISNULL(100*CONVERT(numeric, total_boosters, 0)/population, 0) AS VaccinationPerBooster
FROM PortfolioProject..Covid
WHERE location = 'World'
ORDER BY location, date

SELECT location
	, CONVERT(date, ISNULL(date, 0)) AS Date
	, population
    , CONVERT(numeric, people_vaccinated, 0) AS VaccinationFirst
	, ISNULL(CONVERT(numeric, people_fully_vaccinated, 0),0) AS VaccinationFully
	, ISNULL(CONVERT(numeric, total_boosters, 0),0) AS VaccinationBooster
	, 100*CONVERT(numeric, people_vaccinated, 0)/population AS VaccinationPerFirst
	, ISNULL(100*CONVERT(numeric, people_fully_vaccinated, 0)/population, 0) AS VaccinationPerFully
	, ISNULL(100*CONVERT(numeric, total_boosters, 0)/population, 0) AS VaccinationPerBooster
FROM PortfolioProject..Covid
WHERE location = 'World' AND people_vaccinated IS NOT NULL
ORDER BY date

SELECT *
FROM PortfolioProject..Covid
WHERE location in ('Belarus', 'Russia', 'Ukraine', 'Poland', 'Latvia', 'Lithuania')
ORDER BY location, date


SELECT location
	, CONVERT(date, ISNULL(date, 0)) AS Date
	, ISNULL(CONVERT(numeric, new_deaths, 0), 0) AS New_death
FROM PortfolioProject..Covid
WHERE location = 'World'
ORDER BY location, date