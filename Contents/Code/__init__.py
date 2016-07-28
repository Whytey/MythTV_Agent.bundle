import re
def Start():
	HTTP.CacheTime = CACHE_1DAY
class CustomSportsAgent(Agent.TV_Shows):
	name = 'MythTV'
	languages = [Locale.Language.English]
	primary_provider = True

	def search(self, results, media, lang):
		Log("media.show = " + str(media.show))
		Log("media.name = " + str(media.name))
		Log("media.filename = " + str(media.filename))
		parsedname = str.split(str(media.show),"-..-")
		sport = parsedname[0]
		Log("sport = " + sport)
		if len(parsedname)>1:
			league = parsedname[1]
		else:
			league = parsedname[0]
		Log("league = " + league)
		results.Append(MetadataSearchResult(id=str(media.show),name=league,year=0,score=100,lang=lang))

	def update(self, metadata, media, lang):
		Log("In update!")
		Log(media.title)
		metadata.title = media.title
		metadata.genres = [str.split(str(metadata.id),"-..-")[0]]
		metadata.tags = [str.split(str(metadata.id),"-..-")[0]]
		for episode in media.seasons[1].episodes:
			ep_object = metadata.seasons[1].episodes[episode]
			ep_file = media.seasons[1].episodes[episode].items[0].parts[0].file
			Log(ep_file)
			datematch = re.search('([12][90][0-9][0-9][ \.-][01]?[0-9][ \.-][0-3]?[0-9])', ep_file, re.IGNORECASE)
			if datematch:
				ep_object.originally_available_at = Datetime.ParseDate(datematch.group(1)).date()
			namematch = re.search('(?:[12][90][0-9][0-9][ \.-][01]?[0-9][ \.-][0-3]?[0-9][ \.-]+)([\w \.-]+[\w\. -][Vv][Ss][ \.-][\w\. -]+[\w])(?:\.[\w\D][\w]{1,3}$)', ep_file, re.IGNORECASE)
			if not namematch:
				Log("Name not matched first way")
				namematch = re.search('([\w \.-]+[\w\. -][Vv][Ss][ \.-][\w\. -]+[\w])(?:[ \.-]+[12][90][0-9][0-9][\.-][01]?[0-9][\.-][0-3]?[0-9])', ep_file, re.IGNORECASE)
			if namematch:
				Log("Name matched")
				Log("Match: " + namematch.group(1))
				ep_object.title = namematch.group(1).replace(".", " ").title()
				if datematch:
					ep_object.title = datematch.group(1).replace(".", "-") + " " + ep_object.title