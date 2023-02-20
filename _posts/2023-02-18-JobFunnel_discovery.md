## Experiementation circumventing captchas with JobFunnel.

So, after getting everything setup and ready to go, which was more involved than originally assummed. The
tests were ran, and the result was not a successful one. As the scrape appears to have failed due to some
unknown reason. When the url was opened in a browser to test if the link was good, the page opened without any
error or sign of a captcha. So, it is uncertain if the captcha prevented the scraping or whether it was
something else that interfered with the script. Further testing will be needed to see what is the cause of the
failure.

Output from log.log:

```bash
[2023-02-18 05:50:31,156] [DEBUG] JobFunnel: No master-CSV present, did not update block-list: job_search_results/block_list.json
[2023-02-18 05:50:31,157] [INFO] JobFunnel: Scraping local providers with: ['IndeedScraperUSAEng', 'MonsterScraperUSAEng']
[2023-02-18 05:50:31,303] [DEBUG] IndeedScraperUSAEng: Got Base search results page: https://www.indeed.com/jobs?q=Linux&l=boston%2C+MA&radius=50&limit=50&filter=0
[2023-02-18 05:50:31,307] [ERROR] JobFunnel: Failed to scrape jobs for IndeedScraperUSAEng
[2023-02-18 05:50:31,308] [DEBUG] JobFunnel: Scraped 0 jobs from IndeedScraperUSAEng, took 0.151s
[2023-02-18 05:50:31,312] [INFO] MonsterScraperUSAEng: No get() or set() will be done for Job attrs: ['REMOTENESS']
[2023-02-18 05:50:31,690] [ERROR] JobFunnel: Failed to scrape jobs for MonsterScraperUSAEng
[2023-02-18 05:50:31,690] [DEBUG] JobFunnel: Scraped 0 jobs from MonsterScraperUSAEng, took 0.382s
[2023-02-18 05:50:31,690] [INFO] JobFunnel: Completed all scraping, found 0 new jobs.
[2023-02-18 05:50:31,699] [WARNING] JobFunnel: No new jobs were added to CSV.
```

On a brighter note, while manually checking the url provided by indeed, I noticed connection was routed
through Cloudflare. Although in my tests, cloudflare did not appear to be causing the experienced issues, it
might be worth implementing a mitigation strategy for cloudflare to prevent scraping failures in the future.

So, below are three mitigation tools, which might prove to be useful doing thus.

1. [cfscrape-http-proxy](https://github.com/moonbuggy/cfscrape-http-proxy): Creates a proxy that implements
	 the cloudscraper module. #Active
2. [cloudscraper](https://github.com/VeNoMouS/cloudscraper): Appears to be the only actively developed means
	 to bypass the Cloudflare network as a python module. Implementation method is unknown. Uses the requests
	 library, so using selenium-requests might be an option. #Active #Requests
3. [FlareSolver](https://github.com/FlareSolverr/FlareSolverr): Can only be run in a dockerized container, and
	 is based on nodejs. #Honorable_Mention
