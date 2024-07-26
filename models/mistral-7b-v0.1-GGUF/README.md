<!doctype html>
<html class="">
	<head>
		<meta charset="utf-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no" />
		<meta name="description" content="We’re on a journey to advance and democratize artificial intelligence through open source and open science." />
		<meta property="fb:app_id" content="1321688464574422" />
		<meta name="twitter:card" content="summary_large_image" />
		<meta name="twitter:site" content="@huggingface" />
		<meta property="og:title" content="README.md · TheBloke/Mistral-7B-v0.1-GGUF at main" />
		<meta property="og:type" content="website" />
		<meta property="og:url" content="https://huggingface.co/TheBloke/Mistral-7B-v0.1-GGUF/blob/main/README.md" />
		<meta property="og:image" content="https://cdn-thumbnails.huggingface.co/social-thumbnails/models/TheBloke/Mistral-7B-v0.1-GGUF.png" />

		<link rel="stylesheet" href="/front/build/kube-537c6d6/style.css" />

		<link rel="preconnect" href="https://fonts.gstatic.com" />
		<link
			href="https://fonts.googleapis.com/css2?family=Source+Sans+Pro:ital,wght@0,200;0,300;0,400;0,600;0,700;0,900;1,200;1,300;1,400;1,600;1,700;1,900&display=swap"
			rel="stylesheet"
		/>
		<link
			href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;600;700&display=swap"
			rel="stylesheet"
		/>

		<link
			rel="preload"
			href="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.12.0/katex.min.css"
			as="style"
			onload="this.onload=null;this.rel='stylesheet'"
		/>
		<noscript>
			<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.12.0/katex.min.css" />
		</noscript>

		<link rel="canonical" href="https://huggingface.co/TheBloke/Mistral-7B-v0.1-GGUF/blob/main/README.md">  

		<title>README.md · TheBloke/Mistral-7B-v0.1-GGUF at main</title>

		<script
			defer
			data-domain="huggingface.co"
			event-loggedIn="true"
			src="/js/script.pageview-props.js"
		></script>
		<script>
			window.plausible =
				window.plausible ||
				function () {
					(window.plausible.q = window.plausible.q || []).push(arguments);
				};
		</script>
		<script>
			window.hubConfig = JSON.parse(`{"features":{"signupDisabled":false},"sshGitUrl":"git@hf.co","moonHttpUrl":"https://huggingface.co","captchaApiKey":"bd5f2066-93dc-4bdd-a64b-a24646ca3859","captchaDisabledOnSignup":true,"datasetViewerPublicUrl":"https://datasets-server.huggingface.co","stripePublicKey":"pk_live_x2tdjFXBCvXo2FFmMybezpeM00J6gPCAAc","environment":"production","userAgent":"HuggingFace (production)","spacesIframeDomain":"hf.space","spacesApiUrl":"https://api.hf.space","docSearchKey":"ece5e02e57300e17d152c08056145326e90c4bff3dd07d7d1ae40cf1c8d39cb6","logoDev":{"apiUrl":"https://img.logo.dev/","apiKey":"pk_UHS2HZOeRnaSOdDp7jbd5w"}}`);
		</script>
		<script type="text/javascript" src="https://de5282c3ca0c.edge.sdk.awswaf.com/de5282c3ca0c/526cf06acb0d/challenge.js" defer></script>
	</head>
	<body class="flex flex-col min-h-screen bg-white dark:bg-gray-950 text-black ViewerBlobPage">
		<div class="flex min-h-screen flex-col">
	<div class="SVELTE_HYDRATER contents" data-target="MainHeader" data-props="{&quot;classNames&quot;:&quot;&quot;,&quot;avatarUrl&quot;:&quot;https://cdn-avatars.huggingface.co/v1/production/uploads/noauth/Nv05rEE7v6ZpBWyjodfUT.jpeg&quot;,&quot;isWide&quot;:false,&quot;isZh&quot;:false,&quot;user&quot;:&quot;jeffco&quot;,&quot;unreadNotifications&quot;:0,&quot;csrf&quot;:&quot;eyJkYXRhIjp7ImV4cGlyYXRpb24iOjE3MjIwMzM1NTIzOTksInVzZXJJZCI6IjY0OWRhYTBjYWFjYTVhMjA0NDczMTUyZiJ9LCJzaWduYXR1cmUiOiIxZjI2YjNhOTVlMWQxZWEzZjgzNjM2NWRlMzFmMGNmMTE1NjEwZWRmMzNkODU0MDI4NmE0ZWYwZmRhOTVhMzExIn0=&quot;,&quot;canCreateOrg&quot;:true}"><header class="border-b border-gray-100 "><div class="w-full px-4 container flex h-16 items-center"><div class="flex flex-1 items-center"><a class="mr-5 flex flex-none items-center lg:mr-6" href="/"><img alt="Hugging Face's logo" class="w-7 md:mr-2" src="/front/assets/huggingface_logo-noborder.svg">
				<span class="hidden whitespace-nowrap text-lg font-bold md:block">Hugging Face</span></a>
			<div class="relative flex-1 lg:max-w-sm mr-2 sm:mr-4 md:mr-3 xl:mr-6"><input autocomplete="off" class="w-full dark:bg-gray-950 pl-8 form-input-alt h-9 pr-3 focus:shadow-xl " name="" placeholder="Search models, datasets, users..."   spellcheck="false" type="text" value="">
	<svg class="absolute left-2.5 text-gray-400 top-1/2 transform -translate-y-1/2" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32"><path d="M30 28.59L22.45 21A11 11 0 1 0 21 22.45L28.59 30zM5 14a9 9 0 1 1 9 9a9 9 0 0 1-9-9z" fill="currentColor"></path></svg>
	</div>
			<div class="flex flex-none items-center justify-center p-0.5 place-self-stretch lg:hidden"><button class="relative z-40 flex h-6 w-8 items-center justify-center" type="button"><svg width="1em" height="1em" viewBox="0 0 10 10" class="text-xl" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" preserveAspectRatio="xMidYMid meet" fill="currentColor"><path fill-rule="evenodd" clip-rule="evenodd" d="M1.65039 2.9999C1.65039 2.8066 1.80709 2.6499 2.00039 2.6499H8.00039C8.19369 2.6499 8.35039 2.8066 8.35039 2.9999C8.35039 3.1932 8.19369 3.3499 8.00039 3.3499H2.00039C1.80709 3.3499 1.65039 3.1932 1.65039 2.9999ZM1.65039 4.9999C1.65039 4.8066 1.80709 4.6499 2.00039 4.6499H8.00039C8.19369 4.6499 8.35039 4.8066 8.35039 4.9999C8.35039 5.1932 8.19369 5.3499 8.00039 5.3499H2.00039C1.80709 5.3499 1.65039 5.1932 1.65039 4.9999ZM2.00039 6.6499C1.80709 6.6499 1.65039 6.8066 1.65039 6.9999C1.65039 7.1932 1.80709 7.3499 2.00039 7.3499H8.00039C8.19369 7.3499 8.35039 7.1932 8.35039 6.9999C8.35039 6.8066 8.19369 6.6499 8.00039 6.6499H2.00039Z"></path></svg>
		</button>

	</div></div>
		<nav aria-label="Main" class="ml-auto hidden lg:block"><ul class="flex items-center space-x-1.5 xl:space-x-2"><li><a class="group flex items-center px-2 py-0.5 dark:hover:text-gray-400 hover:text-indigo-700" href="/models"><svg class="mr-1.5 text-gray-400 group-hover:text-indigo-500" style="" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24"><path class="uim-quaternary" d="M20.23 7.24L12 12L3.77 7.24a1.98 1.98 0 0 1 .7-.71L11 2.76c.62-.35 1.38-.35 2 0l6.53 3.77c.29.173.531.418.7.71z" opacity=".25" fill="currentColor"></path><path class="uim-tertiary" d="M12 12v9.5a2.09 2.09 0 0 1-.91-.21L4.5 17.48a2.003 2.003 0 0 1-1-1.73v-7.5a2.06 2.06 0 0 1 .27-1.01L12 12z" opacity=".5" fill="currentColor"></path><path class="uim-primary" d="M20.5 8.25v7.5a2.003 2.003 0 0 1-1 1.73l-6.62 3.82c-.275.13-.576.198-.88.2V12l8.23-4.76c.175.308.268.656.27 1.01z" fill="currentColor"></path></svg>
					Models</a>
			</li><li><a class="group flex items-center px-2 py-0.5 dark:hover:text-gray-400 hover:text-red-700" href="/datasets"><svg class="mr-1.5 text-gray-400 group-hover:text-red-500" style="" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 25 25"><ellipse cx="12.5" cy="5" fill="currentColor" fill-opacity="0.25" rx="7.5" ry="2"></ellipse><path d="M12.5 15C16.6421 15 20 14.1046 20 13V20C20 21.1046 16.6421 22 12.5 22C8.35786 22 5 21.1046 5 20V13C5 14.1046 8.35786 15 12.5 15Z" fill="currentColor" opacity="0.5"></path><path d="M12.5 7C16.6421 7 20 6.10457 20 5V11.5C20 12.6046 16.6421 13.5 12.5 13.5C8.35786 13.5 5 12.6046 5 11.5V5C5 6.10457 8.35786 7 12.5 7Z" fill="currentColor" opacity="0.5"></path><path d="M5.23628 12C5.08204 12.1598 5 12.8273 5 13C5 14.1046 8.35786 15 12.5 15C16.6421 15 20 14.1046 20 13C20 12.8273 19.918 12.1598 19.7637 12C18.9311 12.8626 15.9947 13.5 12.5 13.5C9.0053 13.5 6.06886 12.8626 5.23628 12Z" fill="currentColor"></path></svg>
					Datasets</a>
			</li><li><a class="group flex items-center px-2 py-0.5 dark:hover:text-gray-400 hover:text-blue-700" href="/spaces"><svg class="mr-1.5 text-gray-400 group-hover:text-blue-500" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" viewBox="0 0 25 25"><path opacity=".5" d="M6.016 14.674v4.31h4.31v-4.31h-4.31ZM14.674 14.674v4.31h4.31v-4.31h-4.31ZM6.016 6.016v4.31h4.31v-4.31h-4.31Z" fill="currentColor"></path><path opacity=".75" fill-rule="evenodd" clip-rule="evenodd" d="M3 4.914C3 3.857 3.857 3 4.914 3h6.514c.884 0 1.628.6 1.848 1.414a5.171 5.171 0 0 1 7.31 7.31c.815.22 1.414.964 1.414 1.848v6.514A1.914 1.914 0 0 1 20.086 22H4.914A1.914 1.914 0 0 1 3 20.086V4.914Zm3.016 1.102v4.31h4.31v-4.31h-4.31Zm0 12.968v-4.31h4.31v4.31h-4.31Zm8.658 0v-4.31h4.31v4.31h-4.31Zm0-10.813a2.155 2.155 0 1 1 4.31 0 2.155 2.155 0 0 1-4.31 0Z" fill="currentColor"></path><path opacity=".25" d="M16.829 6.016a2.155 2.155 0 1 0 0 4.31 2.155 2.155 0 0 0 0-4.31Z" fill="currentColor"></path></svg>
					Spaces</a>
			</li><li><a class="group flex items-center px-2 py-0.5 dark:hover:text-gray-400 hover:text-yellow-700" href="/posts"><svg class="mr-1.5 text-gray-400 group-hover:text-yellow-500 !text-yellow-500" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" viewBox="0 0 12 12" preserveAspectRatio="xMidYMid meet"><path fill="currentColor" fill-rule="evenodd" d="M3.73 2.4A4.25 4.25 0 1 1 6 10.26H2.17l-.13-.02a.43.43 0 0 1-.3-.43l.01-.06a.43.43 0 0 1 .12-.22l.84-.84A4.26 4.26 0 0 1 3.73 2.4Z" clip-rule="evenodd"></path></svg>
					Posts</a>
			</li><li><a class="group flex items-center px-2 py-0.5 dark:hover:text-gray-400 hover:text-yellow-700" href="/docs"><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" class="mr-1.5 text-gray-400 group-hover:text-yellow-500" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32"><path opacity="0.5" d="M20.9022 5.10334L10.8012 10.8791L7.76318 9.11193C8.07741 8.56791 8.5256 8.11332 9.06512 7.7914L15.9336 3.73907C17.0868 3.08811 18.5002 3.26422 19.6534 3.91519L19.3859 3.73911C19.9253 4.06087 20.5879 4.56025 20.9022 5.10334Z" fill="currentColor"></path><path d="M10.7999 10.8792V28.5483C10.2136 28.5475 9.63494 28.4139 9.10745 28.1578C8.5429 27.8312 8.074 27.3621 7.74761 26.7975C7.42122 26.2327 7.24878 25.5923 7.24756 24.9402V10.9908C7.25062 10.3319 7.42358 9.68487 7.74973 9.1123L10.7999 10.8792Z" fill="currentColor" fill-opacity="0.75"></path><path fill-rule="evenodd" clip-rule="evenodd" d="M21.3368 10.8499V6.918C21.3331 6.25959 21.16 5.61234 20.8346 5.03949L10.7971 10.8727L10.8046 10.874L21.3368 10.8499Z" fill="currentColor"></path><path opacity="0.5" d="M21.7937 10.8488L10.7825 10.8741V28.5486L21.7937 28.5234C23.3344 28.5234 24.5835 27.2743 24.5835 25.7335V13.6387C24.5835 12.0979 23.4365 11.1233 21.7937 10.8488Z" fill="currentColor"></path></svg>
					Docs</a>
			</li>
		<li class="max-2xl:hidden"><div class="relative ">
	<button class="px-2 py-0.5 group hover:text-green-700 dark:hover:text-gray-400 flex items-center " type="button">
		<svg class="mr-1.5 text-gray-400 group-hover:text-green-500" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24"><path class="uim-tertiary" d="M19 6H5a3 3 0 0 0-3 3v2.72L8.837 14h6.326L22 11.72V9a3 3 0 0 0-3-3z" opacity=".5" fill="currentColor"></path><path class="uim-primary" d="M10 6V5h4v1h2V5a2.002 2.002 0 0 0-2-2h-4a2.002 2.002 0 0 0-2 2v1h2zm-1.163 8L2 11.72V18a3.003 3.003 0 0 0 3 3h14a3.003 3.003 0 0 0 3-3v-6.28L15.163 14H8.837z" fill="currentColor"></path></svg>
			Solutions
		</button>
	
	
	</div></li>
		<li><a class="group flex items-center px-2 py-0.5 hover:text-gray-500 dark:hover:text-gray-400" href="/pricing">Pricing
			</a></li>

		<li><div class="relative group">
	<button class="px-2 py-0.5 hover:text-gray-500 dark:hover:text-gray-600 flex items-center " type="button">
		<svg class=" text-gray-500 w-5 group-hover:text-gray-400 dark:text-gray-300 dark:group-hover:text-gray-400" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" viewBox="0 0 32 18" preserveAspectRatio="xMidYMid meet"><path fill-rule="evenodd" clip-rule="evenodd" d="M14.4504 3.30221C14.4504 2.836 14.8284 2.45807 15.2946 2.45807H28.4933C28.9595 2.45807 29.3374 2.836 29.3374 3.30221C29.3374 3.76842 28.9595 4.14635 28.4933 4.14635H15.2946C14.8284 4.14635 14.4504 3.76842 14.4504 3.30221Z" fill="currentColor"></path><path fill-rule="evenodd" clip-rule="evenodd" d="M14.4504 9.00002C14.4504 8.53382 14.8284 8.15588 15.2946 8.15588H28.4933C28.9595 8.15588 29.3374 8.53382 29.3374 9.00002C29.3374 9.46623 28.9595 9.84417 28.4933 9.84417H15.2946C14.8284 9.84417 14.4504 9.46623 14.4504 9.00002Z" fill="currentColor"></path><path fill-rule="evenodd" clip-rule="evenodd" d="M14.4504 14.6978C14.4504 14.2316 14.8284 13.8537 15.2946 13.8537H28.4933C28.9595 13.8537 29.3374 14.2316 29.3374 14.6978C29.3374 15.164 28.9595 15.542 28.4933 15.542H15.2946C14.8284 15.542 14.4504 15.164 14.4504 14.6978Z" fill="currentColor"></path><path fill-rule="evenodd" clip-rule="evenodd" d="M1.94549 6.87377C2.27514 6.54411 2.80962 6.54411 3.13928 6.87377L6.23458 9.96907L9.32988 6.87377C9.65954 6.54411 10.194 6.54411 10.5237 6.87377C10.8533 7.20343 10.8533 7.73791 10.5237 8.06756L6.23458 12.3567L1.94549 8.06756C1.61583 7.73791 1.61583 7.20343 1.94549 6.87377Z" fill="currentColor"></path></svg>
			
		</button>
	
	
	</div></li>
		<li><hr class="h-5 w-0.5 border-none bg-gray-100 dark:bg-gray-800"></li>
		<li><form action="/logout" method="POST" class="hidden"><input type="hidden" name="csrf" value="eyJkYXRhIjp7ImV4cGlyYXRpb24iOjE3MjIwMzM1NTIzOTksInVzZXJJZCI6IjY0OWRhYTBjYWFjYTVhMjA0NDczMTUyZiJ9LCJzaWduYXR1cmUiOiIxZjI2YjNhOTVlMWQxZWEzZjgzNjM2NWRlMzFmMGNmMTE1NjEwZWRmMzNkODU0MDI4NmE0ZWYwZmRhOTVhMzExIn0="></form>
<div class="relative ml-2 w-[1.38rem] h-[1.38rem] ">
	<button class="ml-auto rounded-full ring-2 group ring-indigo-400 focus:ring-blue-500 hover:ring-offset-1 focus:ring-offset-1 focus:outline-none outline-none dark:ring-offset-gray-950 " type="button">
		
		<div class="relative"><img alt="" class="h-[1.38rem] w-[1.38rem] overflow-hidden rounded-full" src="https://cdn-avatars.huggingface.co/v1/production/uploads/noauth/Nv05rEE7v6ZpBWyjodfUT.jpeg" crossorigin="anonymous">
			</div>
	
		</button>
	
	
	</div></li></ul></nav></div></header></div>
	
	
	
	<div class="SVELTE_HYDRATER contents" data-target="SSOBanner" data-props="{&quot;organizations&quot;:[]}"></div>
	

	<main class="flex flex-1 flex-col"><div class="SVELTE_HYDRATER contents" data-target="ModelHeader" data-props="{&quot;activeTab&quot;:&quot;files&quot;,&quot;authLight&quot;:{&quot;csrfToken&quot;:&quot;eyJkYXRhIjp7ImV4cGlyYXRpb24iOjE3MjIwMzM1NTIzOTksInVzZXJJZCI6IjY0OWRhYTBjYWFjYTVhMjA0NDczMTUyZiJ9LCJzaWduYXR1cmUiOiIxZjI2YjNhOTVlMWQxZWEzZjgzNjM2NWRlMzFmMGNmMTE1NjEwZWRmMzNkODU0MDI4NmE0ZWYwZmRhOTVhMzExIn0=&quot;,&quot;hasHfLevelAccess&quot;:false,&quot;u&quot;:{&quot;avatarUrl&quot;:&quot;https://cdn-avatars.huggingface.co/v1/production/uploads/noauth/Nv05rEE7v6ZpBWyjodfUT.jpeg&quot;,&quot;isPro&quot;:false,&quot;orgs&quot;:[],&quot;user&quot;:&quot;jeffco&quot;,&quot;canPost&quot;:false,&quot;canHaveBilling&quot;:true,&quot;canCreateOrg&quot;:true,&quot;theme&quot;:&quot;light&quot;,&quot;notifications&quot;:{&quot;org_suggestions&quot;:false}}},&quot;author&quot;:{&quot;avatarUrl&quot;:&quot;https://cdn-avatars.huggingface.co/v1/production/uploads/6426d3f3a7723d62b53c259b/tvPikpAzKTKGN5wrpadOJ.jpeg&quot;,&quot;fullname&quot;:&quot;Tom Jobbins&quot;,&quot;name&quot;:&quot;TheBloke&quot;,&quot;type&quot;:&quot;user&quot;,&quot;isPro&quot;:true,&quot;isHf&quot;:false,&quot;isMod&quot;:false},&quot;canReadRepoSettings&quot;:false,&quot;canWriteRepoContent&quot;:false,&quot;canDisable&quot;:false,&quot;model&quot;:{&quot;author&quot;:&quot;TheBloke&quot;,&quot;cardData&quot;:{&quot;base_model&quot;:&quot;mistralai/Mistral-7B-v0.1&quot;,&quot;inference&quot;:false,&quot;license&quot;:&quot;apache-2.0&quot;,&quot;model_creator&quot;:&quot;Mistral AI&quot;,&quot;model_name&quot;:&quot;Mistral 7B v0.1&quot;,&quot;model_type&quot;:&quot;mistral&quot;,&quot;pipeline_tag&quot;:&quot;text-generation&quot;,&quot;prompt_template&quot;:&quot;{prompt}\n&quot;,&quot;quantized_by&quot;:&quot;TheBloke&quot;,&quot;tags&quot;:[&quot;pretrained&quot;]},&quot;cardExists&quot;:true,&quot;config&quot;:{&quot;model_type&quot;:&quot;mistral&quot;},&quot;createdAt&quot;:&quot;2023-09-27T16:17:24.000Z&quot;,&quot;discussionsDisabled&quot;:false,&quot;downloads&quot;:7983,&quot;downloadsAllTime&quot;:53552,&quot;id&quot;:&quot;TheBloke/Mistral-7B-v0.1-GGUF&quot;,&quot;isLikedByUser&quot;:false,&quot;isMutedByUser&quot;:false,&quot;isWatchedByUser&quot;:false,&quot;inference&quot;:&quot;NotSupported_ExplicitOptOut&quot;,&quot;lastModified&quot;:&quot;2023-09-28T22:42:44.000Z&quot;,&quot;likes&quot;:238,&quot;pipeline_tag&quot;:&quot;text-generation&quot;,&quot;library_name&quot;:&quot;transformers&quot;,&quot;librariesOther&quot;:[],&quot;trackDownloads&quot;:true,&quot;model-index&quot;:null,&quot;private&quot;:false,&quot;repoType&quot;:&quot;model&quot;,&quot;gated&quot;:false,&quot;pwcLink&quot;:{&quot;error&quot;:&quot;Unknown error, can't generate link to Papers With Code.&quot;},&quot;tags&quot;:[&quot;transformers&quot;,&quot;gguf&quot;,&quot;mistral&quot;,&quot;pretrained&quot;,&quot;text-generation&quot;,&quot;base_model:mistralai/Mistral-7B-v0.1&quot;,&quot;base_model:quantized:mistralai/Mistral-7B-v0.1&quot;,&quot;license:apache-2.0&quot;,&quot;text-generation-inference&quot;,&quot;region:us&quot;],&quot;tag_objs&quot;:[{&quot;id&quot;:&quot;text-generation&quot;,&quot;label&quot;:&quot;Text Generation&quot;,&quot;type&quot;:&quot;pipeline_tag&quot;,&quot;subType&quot;:&quot;nlp&quot;},{&quot;id&quot;:&quot;transformers&quot;,&quot;label&quot;:&quot;Transformers&quot;,&quot;type&quot;:&quot;library&quot;},{&quot;id&quot;:&quot;gguf&quot;,&quot;label&quot;:&quot;GGUF&quot;,&quot;type&quot;:&quot;library&quot;},{&quot;id&quot;:&quot;mistral&quot;,&quot;label&quot;:&quot;mistral&quot;,&quot;type&quot;:&quot;other&quot;},{&quot;id&quot;:&quot;pretrained&quot;,&quot;label&quot;:&quot;pretrained&quot;,&quot;type&quot;:&quot;other&quot;},{&quot;id&quot;:&quot;base_model:mistralai/Mistral-7B-v0.1&quot;,&quot;label&quot;:&quot;base_model:mistralai/Mistral-7B-v0.1&quot;,&quot;type&quot;:&quot;other&quot;},{&quot;id&quot;:&quot;base_model:quantized:mistralai/Mistral-7B-v0.1&quot;,&quot;label&quot;:&quot;base_model:quantized:mistralai/Mistral-7B-v0.1&quot;,&quot;type&quot;:&quot;other&quot;},{&quot;id&quot;:&quot;text-generation-inference&quot;,&quot;label&quot;:&quot;text-generation-inference&quot;,&quot;type&quot;:&quot;other&quot;},{&quot;id&quot;:&quot;license:apache-2.0&quot;,&quot;label&quot;:&quot;apache-2.0&quot;,&quot;type&quot;:&quot;license&quot;},{&quot;type&quot;:&quot;region&quot;,&quot;label&quot;:&quot;🇺🇸 Region: US&quot;,&quot;id&quot;:&quot;region:us&quot;}],&quot;transformersInfo&quot;:{&quot;auto_model&quot;:&quot;AutoModel&quot;},&quot;widgetData&quot;:[{&quot;text&quot;:&quot;My name is Julien and I like to&quot;},{&quot;text&quot;:&quot;My name is Thomas and my main&quot;},{&quot;text&quot;:&quot;My name is Mariama, my favorite&quot;},{&quot;text&quot;:&quot;My name is Clara and I am&quot;},{&quot;text&quot;:&quot;My name is Lewis and I like to&quot;},{&quot;text&quot;:&quot;My name is Merve and my favorite&quot;},{&quot;text&quot;:&quot;My name is Teven and I am&quot;},{&quot;text&quot;:&quot;Once upon a time,&quot;}],&quot;gguf&quot;:{&quot;total&quot;:7241732096,&quot;architecture&quot;:&quot;llama&quot;},&quot;ggufFilePaths&quot;:[&quot;mistral-7b-v0.1.Q2_K.gguf&quot;,&quot;mistral-7b-v0.1.Q3_K_L.gguf&quot;,&quot;mistral-7b-v0.1.Q3_K_M.gguf&quot;,&quot;mistral-7b-v0.1.Q3_K_S.gguf&quot;,&quot;mistral-7b-v0.1.Q4_0.gguf&quot;,&quot;mistral-7b-v0.1.Q4_K_M.gguf&quot;,&quot;mistral-7b-v0.1.Q4_K_S.gguf&quot;,&quot;mistral-7b-v0.1.Q5_0.gguf&quot;,&quot;mistral-7b-v0.1.Q5_K_M.gguf&quot;,&quot;mistral-7b-v0.1.Q5_K_S.gguf&quot;,&quot;mistral-7b-v0.1.Q6_K.gguf&quot;,&quot;mistral-7b-v0.1.Q8_0.gguf&quot;]},&quot;discussionsStats&quot;:{&quot;closed&quot;:1,&quot;open&quot;:2,&quot;total&quot;:3},&quot;orgs&quot;:[],&quot;query&quot;:{}}"><header class="from-gray-50-to-white border-b border-gray-100 bg-gradient-to-t via-white dark:via-gray-950 pt-6 sm:pt-9"><div class="container relative "><h1 class="flex flex-wrap items-center leading-tight mb-3 text-lg max-sm:gap-y-1.5 md:text-xl">
			<div class="group flex flex-none items-center"><div class="relative mr-1.5 flex items-center">

			<img alt="" class="w-3.5 h-3.5 rounded-full  flex-none" src="https://cdn-avatars.huggingface.co/v1/production/uploads/6426d3f3a7723d62b53c259b/tvPikpAzKTKGN5wrpadOJ.jpeg" crossorigin="anonymous"></div>
		<a href="/TheBloke" class="text-gray-400 hover:text-blue-600">TheBloke</a>
		<div class="mx-0.5 text-gray-300">/</div></div>

<div class="max-w-full "><a class="break-words font-mono font-semibold hover:text-blue-600 " href="/TheBloke/Mistral-7B-v0.1-GGUF">Mistral-7B-v0.1-GGUF</a>
	<button class="relative text-sm mr-4 inline-flex cursor-pointer items-center text-sm focus:outline-none  mx-0.5   text-gray-600 " title="Copy model name to clipboard" type="button"><svg class="" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" fill="currentColor" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32"><path d="M28,10V28H10V10H28m0-2H10a2,2,0,0,0-2,2V28a2,2,0,0,0,2,2H28a2,2,0,0,0,2-2V10a2,2,0,0,0-2-2Z" transform="translate(0)"></path><path d="M4,18H2V4A2,2,0,0,1,4,2H18V4H4Z" transform="translate(0)"></path><rect fill="none" width="32" height="32"></rect></svg>
	
	</button></div>
			<div class="inline-flex items-center overflow-hidden whitespace-nowrap rounded-md border bg-white text-sm leading-none text-gray-500  mr-2"><button class="relative flex items-center overflow-hidden from-red-50 to-transparent dark:from-red-900 px-1.5 py-1 hover:bg-gradient-to-t focus:outline-none"  title="Like"><svg class="left-1.5 absolute" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32" fill="currentColor"><path d="M22.45,6a5.47,5.47,0,0,1,3.91,1.64,5.7,5.7,0,0,1,0,8L16,26.13,5.64,15.64a5.7,5.7,0,0,1,0-8,5.48,5.48,0,0,1,7.82,0L16,10.24l2.53-2.58A5.44,5.44,0,0,1,22.45,6m0-2a7.47,7.47,0,0,0-5.34,2.24L16,7.36,14.89,6.24a7.49,7.49,0,0,0-10.68,0,7.72,7.72,0,0,0,0,10.82L16,29,27.79,17.06a7.72,7.72,0,0,0,0-10.82A7.49,7.49,0,0,0,22.45,4Z"></path></svg>

		
		<span class="ml-4 pl-0.5 ">like</span></button>
	<button class="flex items-center border-l px-1.5 py-1 text-gray-400 hover:bg-gray-50 focus:bg-gray-100 focus:outline-none dark:hover:bg-gray-900 dark:focus:bg-gray-800" title="See users who liked this repository">238</button></div>




			
	</h1>
		<div class="mb-3 flex flex-wrap md:mb-4"><a class="mb-1 mr-1 md:mb-1.5 md:mr-1.5 rounded-lg" href="/models?pipeline_tag=text-generation"><div class="tag tag-white  "><div class="tag-ico -ml-2 tag-ico-indigo"><svg class="" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" fill="currentColor" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 18 18"><path d="M16.2607 8.08202L14.468 6.28928C14.3063 6.12804 14.0873 6.03749 13.859 6.03749C13.6307 6.03749 13.4117 6.12804 13.25 6.28928L5.6375 13.904V16.9125H8.64607L16.2607 9.30002C16.422 9.13836 16.5125 8.91935 16.5125 8.69102C16.5125 8.4627 16.422 8.24369 16.2607 8.08202V8.08202ZM8.1953 15.825H6.725V14.3547L11.858 9.22118L13.3288 10.6915L8.1953 15.825ZM14.0982 9.92262L12.6279 8.45232L13.8606 7.21964L15.3309 8.68994L14.0982 9.92262Z"></path><path d="M6.18125 9.84373H7.26875V6.03748H8.9V4.94998H4.55V6.03748H6.18125V9.84373Z"></path><path d="M4.55 11.475H2.375V2.775H11.075V4.95H12.1625V2.775C12.1625 2.48658 12.0479 2.20997 11.844 2.00602C11.64 1.80208 11.3634 1.6875 11.075 1.6875H2.375C2.08658 1.6875 1.80997 1.80208 1.60602 2.00602C1.40207 2.20997 1.2875 2.48658 1.2875 2.775V11.475C1.2875 11.7634 1.40207 12.04 1.60602 12.244C1.80997 12.4479 2.08658 12.5625 2.375 12.5625H4.55V11.475Z"></path></svg></div>

	

	<span>Text Generation</span>
	

	</div></a><a class="mb-1 mr-1 md:mb-1.5 md:mr-1.5 rounded-lg" href="/models?library=transformers"><div class="tag tag-white  "><svg class="text-black inline-block text-sm" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" preserveAspectRatio="xMidYMid meet" width="1em" height="1em" viewBox="0 0 95 88"><path fill="#fff" d="M94.25 70.08a8.28 8.28 0 0 1-.43 6.46 10.57 10.57 0 0 1-3 3.6 25.18 25.18 0 0 1-5.7 3.2 65.74 65.74 0 0 1-7.56 2.65 46.67 46.67 0 0 1-11.42 1.68c-5.42.05-10.09-1.23-13.4-4.5a40.4 40.4 0 0 1-10.14.03c-3.34 3.25-7.99 4.52-13.39 4.47a46.82 46.82 0 0 1-11.43-1.68 66.37 66.37 0 0 1-7.55-2.65c-2.28-.98-4.17-2-5.68-3.2a10.5 10.5 0 0 1-3.02-3.6c-.99-2-1.18-4.3-.42-6.46a8.54 8.54 0 0 1-.33-5.63c.25-.95.66-1.83 1.18-2.61a8.67 8.67 0 0 1 2.1-8.47 8.23 8.23 0 0 1 2.82-2.07 41.75 41.75 0 1 1 81.3-.12 8.27 8.27 0 0 1 3.11 2.19 8.7 8.7 0 0 1 2.1 8.47c.52.78.93 1.66 1.18 2.61a8.61 8.61 0 0 1-.32 5.63Z"></path><path fill="#FFD21E" d="M47.21 76.5a34.75 34.75 0 1 0 0-69.5 34.75 34.75 0 0 0 0 69.5Z"></path><path fill="#FF9D0B" d="M81.96 41.75a34.75 34.75 0 1 0-69.5 0 34.75 34.75 0 0 0 69.5 0Zm-73.5 0a38.75 38.75 0 1 1 77.5 0 38.75 38.75 0 0 1-77.5 0Z"></path><path fill="#3A3B45" d="M58.5 32.3c1.28.44 1.78 3.06 3.07 2.38a5 5 0 1 0-6.76-2.07c.61 1.15 2.55-.72 3.7-.32ZM34.95 32.3c-1.28.44-1.79 3.06-3.07 2.38a5 5 0 1 1 6.76-2.07c-.61 1.15-2.56-.72-3.7-.32Z"></path><path fill="#FF323D" d="M46.96 56.29c9.83 0 13-8.76 13-13.26 0-2.34-1.57-1.6-4.09-.36-2.33 1.15-5.46 2.74-8.9 2.74-7.19 0-13-6.88-13-2.38s3.16 13.26 13 13.26Z"></path><path fill="#3A3B45" fill-rule="evenodd" d="M39.43 54a8.7 8.7 0 0 1 5.3-4.49c.4-.12.81.57 1.24 1.28.4.68.82 1.37 1.24 1.37.45 0 .9-.68 1.33-1.35.45-.7.89-1.38 1.32-1.25a8.61 8.61 0 0 1 5 4.17c3.73-2.94 5.1-7.74 5.1-10.7 0-2.34-1.57-1.6-4.09-.36l-.14.07c-2.31 1.15-5.39 2.67-8.77 2.67s-6.45-1.52-8.77-2.67c-2.6-1.29-4.23-2.1-4.23.29 0 3.05 1.46 8.06 5.47 10.97Z" clip-rule="evenodd"></path><path fill="#FF9D0B" d="M70.71 37a3.25 3.25 0 1 0 0-6.5 3.25 3.25 0 0 0 0 6.5ZM24.21 37a3.25 3.25 0 1 0 0-6.5 3.25 3.25 0 0 0 0 6.5ZM17.52 48c-1.62 0-3.06.66-4.07 1.87a5.97 5.97 0 0 0-1.33 3.76 7.1 7.1 0 0 0-1.94-.3c-1.55 0-2.95.59-3.94 1.66a5.8 5.8 0 0 0-.8 7 5.3 5.3 0 0 0-1.79 2.82c-.24.9-.48 2.8.8 4.74a5.22 5.22 0 0 0-.37 5.02c1.02 2.32 3.57 4.14 8.52 6.1 3.07 1.22 5.89 2 5.91 2.01a44.33 44.33 0 0 0 10.93 1.6c5.86 0 10.05-1.8 12.46-5.34 3.88-5.69 3.33-10.9-1.7-15.92-2.77-2.78-4.62-6.87-5-7.77-.78-2.66-2.84-5.62-6.25-5.62a5.7 5.7 0 0 0-4.6 2.46c-1-1.26-1.98-2.25-2.86-2.82A7.4 7.4 0 0 0 17.52 48Zm0 4c.51 0 1.14.22 1.82.65 2.14 1.36 6.25 8.43 7.76 11.18.5.92 1.37 1.31 2.14 1.31 1.55 0 2.75-1.53.15-3.48-3.92-2.93-2.55-7.72-.68-8.01.08-.02.17-.02.24-.02 1.7 0 2.45 2.93 2.45 2.93s2.2 5.52 5.98 9.3c3.77 3.77 3.97 6.8 1.22 10.83-1.88 2.75-5.47 3.58-9.16 3.58-3.81 0-7.73-.9-9.92-1.46-.11-.03-13.45-3.8-11.76-7 .28-.54.75-.76 1.34-.76 2.38 0 6.7 3.54 8.57 3.54.41 0 .7-.17.83-.6.79-2.85-12.06-4.05-10.98-8.17.2-.73.71-1.02 1.44-1.02 3.14 0 10.2 5.53 11.68 5.53.11 0 .2-.03.24-.1.74-1.2.33-2.04-4.9-5.2-5.21-3.16-8.88-5.06-6.8-7.33.24-.26.58-.38 1-.38 3.17 0 10.66 6.82 10.66 6.82s2.02 2.1 3.25 2.1c.28 0 .52-.1.68-.38.86-1.46-8.06-8.22-8.56-11.01-.34-1.9.24-2.85 1.31-2.85Z"></path><path fill="#FFD21E" d="M38.6 76.69c2.75-4.04 2.55-7.07-1.22-10.84-3.78-3.77-5.98-9.3-5.98-9.3s-.82-3.2-2.69-2.9c-1.87.3-3.24 5.08.68 8.01 3.91 2.93-.78 4.92-2.29 2.17-1.5-2.75-5.62-9.82-7.76-11.18-2.13-1.35-3.63-.6-3.13 2.2.5 2.79 9.43 9.55 8.56 11-.87 1.47-3.93-1.71-3.93-1.71s-9.57-8.71-11.66-6.44c-2.08 2.27 1.59 4.17 6.8 7.33 5.23 3.16 5.64 4 4.9 5.2-.75 1.2-12.28-8.53-13.36-4.4-1.08 4.11 11.77 5.3 10.98 8.15-.8 2.85-9.06-5.38-10.74-2.18-1.7 3.21 11.65 6.98 11.76 7.01 4.3 1.12 15.25 3.49 19.08-2.12Z"></path><path fill="#FF9D0B" d="M77.4 48c1.62 0 3.07.66 4.07 1.87a5.97 5.97 0 0 1 1.33 3.76 7.1 7.1 0 0 1 1.95-.3c1.55 0 2.95.59 3.94 1.66a5.8 5.8 0 0 1 .8 7 5.3 5.3 0 0 1 1.78 2.82c.24.9.48 2.8-.8 4.74a5.22 5.22 0 0 1 .37 5.02c-1.02 2.32-3.57 4.14-8.51 6.1-3.08 1.22-5.9 2-5.92 2.01a44.33 44.33 0 0 1-10.93 1.6c-5.86 0-10.05-1.8-12.46-5.34-3.88-5.69-3.33-10.9 1.7-15.92 2.78-2.78 4.63-6.87 5.01-7.77.78-2.66 2.83-5.62 6.24-5.62a5.7 5.7 0 0 1 4.6 2.46c1-1.26 1.98-2.25 2.87-2.82A7.4 7.4 0 0 1 77.4 48Zm0 4c-.51 0-1.13.22-1.82.65-2.13 1.36-6.25 8.43-7.76 11.18a2.43 2.43 0 0 1-2.14 1.31c-1.54 0-2.75-1.53-.14-3.48 3.91-2.93 2.54-7.72.67-8.01a1.54 1.54 0 0 0-.24-.02c-1.7 0-2.45 2.93-2.45 2.93s-2.2 5.52-5.97 9.3c-3.78 3.77-3.98 6.8-1.22 10.83 1.87 2.75 5.47 3.58 9.15 3.58 3.82 0 7.73-.9 9.93-1.46.1-.03 13.45-3.8 11.76-7-.29-.54-.75-.76-1.34-.76-2.38 0-6.71 3.54-8.57 3.54-.42 0-.71-.17-.83-.6-.8-2.85 12.05-4.05 10.97-8.17-.19-.73-.7-1.02-1.44-1.02-3.14 0-10.2 5.53-11.68 5.53-.1 0-.19-.03-.23-.1-.74-1.2-.34-2.04 4.88-5.2 5.23-3.16 8.9-5.06 6.8-7.33-.23-.26-.57-.38-.98-.38-3.18 0-10.67 6.82-10.67 6.82s-2.02 2.1-3.24 2.1a.74.74 0 0 1-.68-.38c-.87-1.46 8.05-8.22 8.55-11.01.34-1.9-.24-2.85-1.31-2.85Z"></path><path fill="#FFD21E" d="M56.33 76.69c-2.75-4.04-2.56-7.07 1.22-10.84 3.77-3.77 5.97-9.3 5.97-9.3s.82-3.2 2.7-2.9c1.86.3 3.23 5.08-.68 8.01-3.92 2.93.78 4.92 2.28 2.17 1.51-2.75 5.63-9.82 7.76-11.18 2.13-1.35 3.64-.6 3.13 2.2-.5 2.79-9.42 9.55-8.55 11 .86 1.47 3.92-1.71 3.92-1.71s9.58-8.71 11.66-6.44c2.08 2.27-1.58 4.17-6.8 7.33-5.23 3.16-5.63 4-4.9 5.2.75 1.2 12.28-8.53 13.36-4.4 1.08 4.11-11.76 5.3-10.97 8.15.8 2.85 9.05-5.38 10.74-2.18 1.69 3.21-11.65 6.98-11.76 7.01-4.31 1.12-15.26 3.49-19.08-2.12Z"></path></svg>

	

	<span>Transformers</span>
	

	</div></a><a class="mb-1 mr-1 md:mb-1.5 md:mr-1.5 rounded-lg" href="/models?library=gguf"><div class="tag tag-white  "><svg class="text-black inline-block text-sm" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 17 14"><path fill-rule="evenodd" clip-rule="evenodd" d="M2.668 1.076v1.078H1.5v9.692h1.168v1.078h11.666v-1.078H15.5V2.154h-1.166V1.076Zm.986 1.615h4.307v2.694H6.885V3.77H4.732v4.306h2.153V7H5.809V5.924H7.96v3.23H3.654ZM9.04 4.846h4.309v2.691H12.27V5.924h-2.155v4.306h2.155V9.154h-1.077V8.076h2.155v3.233H9.039Z" fill="currentColor"></path></svg>

	

	<span>GGUF</span>
	

	</div></a><a class="mb-1 mr-1 md:mb-1.5 md:mr-1.5 rounded-lg" href="/models?other=mistral"><div class="tag tag-white  ">

	

	<span>mistral</span>
	

	</div></a><a class="mb-1 mr-1 md:mb-1.5 md:mr-1.5 rounded-lg" href="/models?other=pretrained"><div class="tag tag-white  ">

	

	<span>pretrained</span>
	

	</div></a><a class="mb-1 mr-1 md:mb-1.5 md:mr-1.5 rounded-lg" href="/models?other=text-generation-inference"><div class="tag tag-white  ">
		<svg class="" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 12 12"><path fill="#23B0FF" d="m9.6 3.6-3.2-2a1 1 0 0 0-1.1 0L2 3.7a1 1 0 0 0-.3 1.6H10a1 1 0 0 0-.3-1.6Z"></path><path fill="#2094FF" d="m6.7 9.7 3.2-4.5-.4-.8H5.7v4.8l1 .5Z"></path><path fill="#6BCAFF" d="M4.9 9.7 1.7 5.2l.4-.8h3.8v4.8l-1 .5Z"></path><path fill="#000" fill-rule="evenodd" d="M9.9 3.2c.8.5 1 1.5.5 2.3L7 10c-.6.9-2 .9-2.6 0L1.3 5.5c-.5-.8-.3-1.8.5-2.3l3.2-2c.5-.3 1.2-.3 1.7 0l3.2 2ZM6.4 5h3l-3 4.2V5ZM5.3 5h-3l3 4.2V5Zm3.8-1L6 2a.5.5 0 0 0-.5 0L2.6 4H9Z" clip-rule="evenodd"></path></svg>

	

	<span>text-generation-inference</span>
	

	</div></a><div class="relative inline-block ">
	<button class="group mr-1 mb-1 md:mr-1.5 md:mb-1.5  rounded-full rounded-br-none " type="button">
		<div class="tag tag-white rounded-full relative rounded-br-none pr-2.5">
		<svg class="text-xs text-gray-900" width="1em" height="1em" viewBox="0 0 10 10" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M1.46009 5.0945V6.88125C1.46009 7.25201 1.75937 7.55129 2.13012 7.55129C2.50087 7.55129 2.80016 7.25201 2.80016 6.88125V5.0945C2.80016 4.72375 2.50087 4.42446 2.13012 4.42446C1.75937 4.42446 1.46009 4.72375 1.46009 5.0945ZM4.14022 5.0945V6.88125C4.14022 7.25201 4.4395 7.55129 4.81026 7.55129C5.18101 7.55129 5.48029 7.25201 5.48029 6.88125V5.0945C5.48029 4.72375 5.18101 4.42446 4.81026 4.42446C4.4395 4.42446 4.14022 4.72375 4.14022 5.0945ZM1.23674 9.78473H8.38377C8.75452 9.78473 9.0538 9.48545 9.0538 9.1147C9.0538 8.74395 8.75452 8.44466 8.38377 8.44466H1.23674C0.865993 8.44466 0.566711 8.74395 0.566711 9.1147C0.566711 9.48545 0.865993 9.78473 1.23674 9.78473ZM6.82036 5.0945V6.88125C6.82036 7.25201 7.11964 7.55129 7.49039 7.55129C7.86114 7.55129 8.16042 7.25201 8.16042 6.88125V5.0945C8.16042 4.72375 7.86114 4.42446 7.49039 4.42446C7.11964 4.42446 6.82036 4.72375 6.82036 5.0945ZM4.39484 0.623142L0.865993 2.48137C0.682851 2.57517 0.566711 2.76725 0.566711 2.97273C0.566711 3.28094 0.816857 3.53109 1.12507 3.53109H8.49991C8.80365 3.53109 9.0538 3.28094 9.0538 2.97273C9.0538 2.76725 8.93766 2.57517 8.75452 2.48137L5.22568 0.623142C4.9666 0.484669 4.65391 0.484669 4.39484 0.623142V0.623142Z" fill="currentColor"></path></svg>

	<span class="-mr-1 text-gray-400">License:</span>

	<span>apache-2.0</span>
	

	<div class="border-br-gray-200 absolute bottom-0.5 right-0.5 h-1 w-1 border-[3px] border-l-transparent border-t-transparent border-b-gray-200 border-r-gray-200 dark:border-b-gray-700 dark:border-r-gray-700"></div></div>
		
		</button>
	
	
	</div></div>

		<div class="flex flex-col-reverse lg:flex-row lg:items-center lg:justify-between"><div class="-mb-px flex h-12 items-center overflow-x-auto overflow-y-hidden "><a class="tab-alternate " href="/TheBloke/Mistral-7B-v0.1-GGUF"><svg class="mr-1.5 text-gray-400 flex-none" style="" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24"><path class="uim-quaternary" d="M20.23 7.24L12 12L3.77 7.24a1.98 1.98 0 0 1 .7-.71L11 2.76c.62-.35 1.38-.35 2 0l6.53 3.77c.29.173.531.418.7.71z" opacity=".25" fill="currentColor"></path><path class="uim-tertiary" d="M12 12v9.5a2.09 2.09 0 0 1-.91-.21L4.5 17.48a2.003 2.003 0 0 1-1-1.73v-7.5a2.06 2.06 0 0 1 .27-1.01L12 12z" opacity=".5" fill="currentColor"></path><path class="uim-primary" d="M20.5 8.25v7.5a2.003 2.003 0 0 1-1 1.73l-6.62 3.82c-.275.13-.576.198-.88.2V12l8.23-4.76c.175.308.268.656.27 1.01z" fill="currentColor"></path></svg>
			Model card
			
			
		</a><a class="tab-alternate active" href="/TheBloke/Mistral-7B-v0.1-GGUF/tree/main"><svg class="mr-1.5 text-gray-400 flex-none" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24"><path class="uim-tertiary" d="M21 19h-8a1 1 0 0 1 0-2h8a1 1 0 0 1 0 2zm0-4h-8a1 1 0 0 1 0-2h8a1 1 0 0 1 0 2zm0-8h-8a1 1 0 0 1 0-2h8a1 1 0 0 1 0 2zm0 4h-8a1 1 0 0 1 0-2h8a1 1 0 0 1 0 2z" opacity=".5" fill="currentColor"></path><path class="uim-primary" d="M9 19a1 1 0 0 1-1-1V6a1 1 0 0 1 2 0v12a1 1 0 0 1-1 1zm-6-4.333a1 1 0 0 1-.64-1.769L3.438 12l-1.078-.898a1 1 0 0 1 1.28-1.538l2 1.667a1 1 0 0 1 0 1.538l-2 1.667a.999.999 0 0 1-.64.231z" fill="currentColor"></path></svg>
			<span class="xl:hidden">Files</span>
				<span class="hidden xl:inline">Files and versions</span>
			
			
		</a><a class="tab-alternate " href="/TheBloke/Mistral-7B-v0.1-GGUF/discussions"><svg class="mr-1.5 text-gray-400 flex-none" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32"><path d="M20.6081 3C21.7684 3 22.8053 3.49196 23.5284 4.38415C23.9756 4.93678 24.4428 5.82749 24.4808 7.16133C24.9674 7.01707 25.4353 6.93643 25.8725 6.93643C26.9833 6.93643 27.9865 7.37587 28.696 8.17411C29.6075 9.19872 30.0124 10.4579 29.8361 11.7177C29.7523 12.3177 29.5581 12.8555 29.2678 13.3534C29.8798 13.8646 30.3306 14.5763 30.5485 15.4322C30.719 16.1032 30.8939 17.5006 29.9808 18.9403C30.0389 19.0342 30.0934 19.1319 30.1442 19.2318C30.6932 20.3074 30.7283 21.5229 30.2439 22.6548C29.5093 24.3704 27.6841 25.7219 24.1397 27.1727C21.9347 28.0753 19.9174 28.6523 19.8994 28.6575C16.9842 29.4379 14.3477 29.8345 12.0653 29.8345C7.87017 29.8345 4.8668 28.508 3.13831 25.8921C0.356375 21.6797 0.754104 17.8269 4.35369 14.1131C6.34591 12.058 7.67023 9.02782 7.94613 8.36275C8.50224 6.39343 9.97271 4.20438 12.4172 4.20438H12.4179C12.6236 4.20438 12.8314 4.2214 13.0364 4.25468C14.107 4.42854 15.0428 5.06476 15.7115 6.02205C16.4331 5.09583 17.134 4.359 17.7682 3.94323C18.7242 3.31737 19.6794 3 20.6081 3ZM20.6081 5.95917C20.2427 5.95917 19.7963 6.1197 19.3039 6.44225C17.7754 7.44319 14.8258 12.6772 13.7458 14.7131C13.3839 15.3952 12.7655 15.6837 12.2086 15.6837C11.1036 15.6837 10.2408 14.5497 12.1076 13.1085C14.9146 10.9402 13.9299 7.39584 12.5898 7.1776C12.5311 7.16799 12.4731 7.16355 12.4172 7.16355C11.1989 7.16355 10.6615 9.33114 10.6615 9.33114C10.6615 9.33114 9.0863 13.4148 6.38031 16.206C3.67434 18.998 3.5346 21.2388 5.50675 24.2246C6.85185 26.2606 9.42666 26.8753 12.0653 26.8753C14.8021 26.8753 17.6077 26.2139 19.1799 25.793C19.2574 25.7723 28.8193 22.984 27.6081 20.6107C27.4046 20.212 27.0693 20.0522 26.6471 20.0522C24.9416 20.0522 21.8393 22.6726 20.5057 22.6726C20.2076 22.6726 19.9976 22.5416 19.9116 22.222C19.3433 20.1173 28.552 19.2325 27.7758 16.1839C27.639 15.6445 27.2677 15.4256 26.746 15.4263C24.4923 15.4263 19.4358 19.5181 18.3759 19.5181C18.2949 19.5181 18.2368 19.4937 18.2053 19.4419C17.6743 18.557 17.9653 17.9394 21.7082 15.6009C25.4511 13.2617 28.0783 11.8545 26.5841 10.1752C26.4121 9.98141 26.1684 9.8956 25.8725 9.8956C23.6001 9.89634 18.2311 14.9403 18.2311 14.9403C18.2311 14.9403 16.7821 16.496 15.9057 16.496C15.7043 16.496 15.533 16.4139 15.4169 16.2112C14.7956 15.1296 21.1879 10.1286 21.5484 8.06535C21.7928 6.66715 21.3771 5.95917 20.6081 5.95917Z" fill="#FF9D00"></path><path d="M5.50686 24.2246C3.53472 21.2387 3.67446 18.9979 6.38043 16.206C9.08641 13.4147 10.6615 9.33111 10.6615 9.33111C10.6615 9.33111 11.2499 6.95933 12.59 7.17757C13.93 7.39581 14.9139 10.9401 12.1069 13.1084C9.29997 15.276 12.6659 16.7489 13.7459 14.713C14.8258 12.6772 17.7747 7.44316 19.304 6.44221C20.8326 5.44128 21.9089 6.00204 21.5484 8.06532C21.188 10.1286 14.795 15.1295 15.4171 16.2118C16.0391 17.2934 18.2312 14.9402 18.2312 14.9402C18.2312 14.9402 25.0907 8.49588 26.5842 10.1752C28.0776 11.8545 25.4512 13.2616 21.7082 15.6008C17.9646 17.9393 17.6744 18.557 18.2054 19.4418C18.7372 20.3266 26.9998 13.1351 27.7759 16.1838C28.5513 19.2324 19.3434 20.1173 19.9117 22.2219C20.48 24.3274 26.3979 18.2382 27.6082 20.6107C28.8193 22.9839 19.2574 25.7722 19.18 25.7929C16.0914 26.62 8.24723 28.3726 5.50686 24.2246Z" fill="#FFD21E"></path></svg>
			Community
			<div class="ml-1.5 flex h-4 min-w-[1rem] items-center justify-center rounded px-1 text-xs leading-none shadow-sm bg-black text-white dark:bg-gray-800 dark:text-gray-200">3
				</div>
			
		</a>
	</div>
	
			


<div class="relative mb-1.5 flex flex-wrap gap-1.5 sm:flex-nowrap lg:mb-0"><div class="order-last sm:order-first"><div class="relative ">
	<button class="btn px-1.5 py-1.5 " type="button">
		
			<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" class="p-0.5" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32"><circle cx="16" cy="7" r="3" fill="currentColor"></circle><circle cx="16" cy="16" r="3" fill="currentColor"></circle><circle cx="16" cy="25" r="3" fill="currentColor"></circle></svg>
		
		</button>
	
	
	</div></div>















	<div class="flex-none w-full sm:w-auto"><div class="relative ">
	<button class="text-sm btn btn w-full cursor-pointer text-sm" type="button">
		<svg class="mr-1.5 " xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32"><path d="M12.1 2a9.8 9.8 0 0 0-5.4 1.6l6.4 6.4a2.1 2.1 0 0 1 .2 3a2.1 2.1 0 0 1-3-.2L3.7 6.4A9.84 9.84 0 0 0 2 12.1a10.14 10.14 0 0 0 10.1 10.1a10.9 10.9 0 0 0 2.6-.3l6.7 6.7a5 5 0 0 0 7.1-7.1l-6.7-6.7a10.9 10.9 0 0 0 .3-2.6A10 10 0 0 0 12.1 2zm8 10.1a7.61 7.61 0 0 1-.3 2.1l-.3 1.1l.8.8l6.7 6.7a2.88 2.88 0 0 1 .9 2.1A2.72 2.72 0 0 1 27 27a2.9 2.9 0 0 1-4.2 0l-6.7-6.7l-.8-.8l-1.1.3a7.61 7.61 0 0 1-2.1.3a8.27 8.27 0 0 1-5.7-2.3A7.63 7.63 0 0 1 4 12.1a8.33 8.33 0 0 1 .3-2.2l4.4 4.4a4.14 4.14 0 0 0 5.9.2a4.14 4.14 0 0 0-.2-5.9L10 4.2a6.45 6.45 0 0 1 2-.3a8.27 8.27 0 0 1 5.7 2.3a8.49 8.49 0 0 1 2.4 5.9z" fill="currentColor"></path></svg>
			Train
		<svg class="-mr-1 text-gray-500" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24"><path d="M16.293 9.293L12 13.586L7.707 9.293l-1.414 1.414L12 16.414l5.707-5.707z" fill="currentColor"></path></svg></button>
	
	
	</div>
		


		


		

</div>
	<div class="flex-none w-full sm:w-auto"><div class="relative ">
	<button class="text-sm btn btn w-full cursor-pointer text-sm" type="button">
		<svg class="mr-1.5 " xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" fill="currentColor" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32"><rect x="6.34" y="19" width="11.31" height="2" transform="translate(-10.63 14.34) rotate(-45)"></rect><path d="M17,30a1,1,0,0,1-.37-.07,1,1,0,0,1-.62-.79l-1-7,2-.28.75,5.27L21,24.52V17a1,1,0,0,1,.29-.71l4.07-4.07A8.94,8.94,0,0,0,28,5.86V4H26.14a8.94,8.94,0,0,0-6.36,2.64l-4.07,4.07A1,1,0,0,1,15,11H7.48L4.87,14.26l5.27.75-.28,2-7-1a1,1,0,0,1-.79-.62,1,1,0,0,1,.15-1l4-5A1,1,0,0,1,7,9h7.59l3.77-3.78A10.92,10.92,0,0,1,26.14,2H28a2,2,0,0,1,2,2V5.86a10.92,10.92,0,0,1-3.22,7.78L23,17.41V25a1,1,0,0,1-.38.78l-5,4A1,1,0,0,1,17,30Z"></path></svg>
			Deploy
		<svg class="-mr-1 text-gray-500" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24"><path d="M16.293 9.293L12 13.586L7.707 9.293l-1.414 1.414L12 16.414l5.707-5.707z" fill="currentColor"></path></svg></button>
	
	
	</div>
		


		


		


		


		

</div>
	<div class="relative flex-auto sm:flex-none">
	<button class="!from-gray-800 !to-black !text-white !gap-1 !border-gray-800 dark:!border-gray-900  btn w-full cursor-pointer text-sm" type="button">
		<svg class="mr-1.5 !mr-0.5 " xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32"><path fill="currentColor" d="M28 4H4a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h8v4H8v2h16v-2h-4v-4h8a2 2 0 0 0 2-2V6a2 2 0 0 0-2-2ZM18 28h-4v-4h4Zm10-6H4V6h24Z"></path></svg>
			Use this model
		<svg class="-mr-1 text-gray-500" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24"><path d="M16.293 9.293L12 13.586L7.707 9.293l-1.414 1.414L12 16.414l5.707-5.707z" fill="currentColor"></path></svg></button>
	
	
	</div>

</div>
	</div></div></header></div>
	
<div class="container relative flex flex-col md:grid md:space-y-0 w-full md:grid-cols-12  space-y-4 md:gap-6 mb-16"><section class="pt-8 border-gray-100 col-span-full"><header class="flex flex-wrap items-center justify-start pb-2 md:justify-end lg:flex-nowrap"><div class="relative mr-4 flex min-w-0 basis-auto flex-wrap items-center md:flex-grow md:basis-full lg:basis-auto lg:flex-nowrap"><div class="SVELTE_HYDRATER contents" data-target="BranchSelector" data-props="{&quot;path&quot;:&quot;README.md&quot;,&quot;repoName&quot;:&quot;TheBloke/Mistral-7B-v0.1-GGUF&quot;,&quot;repoType&quot;:&quot;model&quot;,&quot;rev&quot;:&quot;main&quot;,&quot;refs&quot;:{&quot;branches&quot;:[{&quot;name&quot;:&quot;main&quot;,&quot;ref&quot;:&quot;refs/heads/main&quot;,&quot;targetCommit&quot;:&quot;d4ae605152c8de0d6570cf624c083fa57dd0d551&quot;}],&quot;tags&quot;:[],&quot;converts&quot;:[]},&quot;view&quot;:&quot;blob&quot;}"><div class="relative mr-4 mb-2">
	<button class="text-sm md:text-base btn w-full cursor-pointer text-sm" type="button">
		<svg class="mr-1.5 text-gray-700 dark:text-gray-400" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24" style="transform: rotate(360deg);"><path d="M13 14c-3.36 0-4.46 1.35-4.82 2.24C9.25 16.7 10 17.76 10 19a3 3 0 0 1-3 3a3 3 0 0 1-3-3c0-1.31.83-2.42 2-2.83V7.83A2.99 2.99 0 0 1 4 5a3 3 0 0 1 3-3a3 3 0 0 1 3 3c0 1.31-.83 2.42-2 2.83v5.29c.88-.65 2.16-1.12 4-1.12c2.67 0 3.56-1.34 3.85-2.23A3.006 3.006 0 0 1 14 7a3 3 0 0 1 3-3a3 3 0 0 1 3 3c0 1.34-.88 2.5-2.09 2.86C17.65 11.29 16.68 14 13 14m-6 4a1 1 0 0 0-1 1a1 1 0 0 0 1 1a1 1 0 0 0 1-1a1 1 0 0 0-1-1M7 4a1 1 0 0 0-1 1a1 1 0 0 0 1 1a1 1 0 0 0 1-1a1 1 0 0 0-1-1m10 2a1 1 0 0 0-1 1a1 1 0 0 0 1 1a1 1 0 0 0 1-1a1 1 0 0 0-1-1z" fill="currentColor"></path></svg>
			main
		<svg class="-mr-1 text-gray-500" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24"><path d="M16.293 9.293L12 13.586L7.707 9.293l-1.414 1.414L12 16.414l5.707-5.707z" fill="currentColor"></path></svg></button>
	
	
	</div></div>
		<div class="relative mb-2 flex flex-wrap items-center"><a class="truncate text-gray-800 hover:underline" href="/TheBloke/Mistral-7B-v0.1-GGUF/tree/main">Mistral-7B-v0.1-GGUF</a>
			<span class="mx-1 text-gray-300">/</span>
				<span class="dark:text-gray-300">README.md</span>
				<div class="SVELTE_HYDRATER contents" data-target="CopyButton" data-props="{&quot;value&quot;:&quot;README.md&quot;,&quot;classNames&quot;:&quot;text-xs ml-2&quot;,&quot;title&quot;:&quot;Copy path&quot;}"><button class="relative text-xs ml-2 inline-flex cursor-pointer items-center text-sm focus:outline-none  mx-0.5   text-gray-600 " title="Copy path" type="button"><svg class="" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" fill="currentColor" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32"><path d="M28,10V28H10V10H28m0-2H10a2,2,0,0,0-2,2V28a2,2,0,0,0,2,2H28a2,2,0,0,0,2-2V10a2,2,0,0,0-2-2Z" transform="translate(0)"></path><path d="M4,18H2V4A2,2,0,0,1,4,2H18V4H4Z" transform="translate(0)"></path><rect fill="none" width="32" height="32"></rect></svg>
	
	</button></div></div></div>

	
	</header>
			<div class="SVELTE_HYDRATER contents" data-target="LastCommit" data-props="{&quot;commitLast&quot;:{&quot;date&quot;:&quot;2023-09-28T22:42:44.000Z&quot;,&quot;subject&quot;:&quot;Update README.md&quot;,&quot;authors&quot;:[{&quot;_id&quot;:&quot;6426d3f3a7723d62b53c259b&quot;,&quot;avatar&quot;:&quot;https://cdn-avatars.huggingface.co/v1/production/uploads/6426d3f3a7723d62b53c259b/tvPikpAzKTKGN5wrpadOJ.jpeg&quot;,&quot;isHf&quot;:false,&quot;user&quot;:&quot;TheBloke&quot;}],&quot;commit&quot;:{&quot;id&quot;:&quot;d4ae605152c8de0d6570cf624c083fa57dd0d551&quot;,&quot;parentIds&quot;:[&quot;9cf2f51f523d69129f81e3f03ce0b845b7a50149&quot;]},&quot;title&quot;:&quot;Update README.md&quot;},&quot;repo&quot;:{&quot;name&quot;:&quot;TheBloke/Mistral-7B-v0.1-GGUF&quot;,&quot;type&quot;:&quot;model&quot;}}"><div class="from-gray-100-to-white flex items-baseline rounded-t-lg border border-b-0 bg-gradient-to-t px-3 py-2 dark:border-gray-800"><img class="mr-2.5 mt-0.5 h-4 w-4 self-center rounded-full" alt="TheBloke's picture" src="https://cdn-avatars.huggingface.co/v1/production/uploads/6426d3f3a7723d62b53c259b/tvPikpAzKTKGN5wrpadOJ.jpeg">
			<div class="mr-5 flex flex-none items-center truncate"><a class="hover:underline" href="/TheBloke">TheBloke
					</a>
				
			</div>
		<div class="mr-4 truncate font-mono text-sm text-gray-500 hover:prose-a:underline"><!-- HTML_TAG_START -->Update README.md<!-- HTML_TAG_END --></div>
		<a class="rounded border bg-gray-50 px-1.5 text-sm hover:underline dark:border-gray-800 dark:bg-gray-900" href="/TheBloke/Mistral-7B-v0.1-GGUF/commit/d4ae605152c8de0d6570cf624c083fa57dd0d551">d4ae605</a>
		
		<time class="ml-auto hidden flex-none truncate pl-2 text-gray-500 dark:text-gray-400 lg:block" datetime="2023-09-28T22:42:44" title="Thu, 28 Sep 2023 22:42:44 GMT">10 months ago</time></div></div>
			<div class="flex flex-wrap items-center border px-3 py-1.5 text-sm text-gray-800 dark:border-gray-800 dark:bg-gray-900"><div class="flex items-center gap-3 text-sm font-medium"><a class="rounded-md px-1.5 capitalize bg-gray-200 dark:bg-gray-800" href="/TheBloke/Mistral-7B-v0.1-GGUF/blob/main/README.md">preview</a>
						<a class="rounded-md px-1.5 capitalize " href="/TheBloke/Mistral-7B-v0.1-GGUF/blob/main/README.md?code=true">code</a></div>
					<div class="mx-4 text-gray-200">|</div>
				<a class="my-1 mr-4 flex items-center hover:underline " href="/TheBloke/Mistral-7B-v0.1-GGUF/raw/main/README.md"><svg class="mr-1.5" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32" style="transform: rotate(360deg);"><path d="M31 16l-7 7l-1.41-1.41L28.17 16l-5.58-5.59L24 9l7 7z" fill="currentColor"></path><path d="M1 16l7-7l1.41 1.41L3.83 16l5.58 5.59L8 23l-7-7z" fill="currentColor"></path><path d="M12.419 25.484L17.639 6l1.932.518L14.35 26z" fill="currentColor"></path></svg>
							raw
						</a><div class="SVELTE_HYDRATER contents" data-target="CopyButton" data-props="{&quot;value&quot;:&quot;https://huggingface.co/TheBloke/Mistral-7B-v0.1-GGUF/resolve/main/README.md&quot;,&quot;style&quot;:&quot;blank&quot;,&quot;label&quot;:&quot;Copy download link&quot;,&quot;classNames&quot;:&quot;my-1 mr-4 flex items-center no-underline hover:underline&quot;}"><button class="relative my-1 mr-4 flex items-center no-underline hover:underline       " title="Copy download link" type="button"><svg class="" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" fill="currentColor" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32"><path d="M28,10V28H10V10H28m0-2H10a2,2,0,0,0-2,2V28a2,2,0,0,0,2,2H28a2,2,0,0,0,2-2V10a2,2,0,0,0-2-2Z" transform="translate(0)"></path><path d="M4,18H2V4A2,2,0,0,1,4,2H18V4H4Z" transform="translate(0)"></path><rect fill="none" width="32" height="32"></rect></svg>
	<span class="ml-1.5 ">Copy download link</span>
	</button></div><a class="my-1 mr-4 flex items-center hover:underline " href="/TheBloke/Mistral-7B-v0.1-GGUF/commits/main/README.md"><svg class="mr-1.5" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32" style="transform: rotate(360deg);"><path d="M16 4C9.383 4 4 9.383 4 16s5.383 12 12 12s12-5.383 12-12S22.617 4 16 4zm0 2c5.535 0 10 4.465 10 10s-4.465 10-10 10S6 21.535 6 16S10.465 6 16 6zm-1 2v9h7v-2h-5V8z" fill="currentColor"></path></svg>
							history
						</a><a class="my-1 mr-4 flex items-center hover:underline " href="/TheBloke/Mistral-7B-v0.1-GGUF/blame/main/README.md"><svg class="mr-1.5" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32" style="transform: rotate(360deg);"><path d="M16 2a14 14 0 1 0 14 14A14 14 0 0 0 16 2zm0 26a12 12 0 1 1 12-12a12 12 0 0 1-12 12z" fill="currentColor"></path><path d="M11.5 11a2.5 2.5 0 1 0 2.5 2.5a2.48 2.48 0 0 0-2.5-2.5z" fill="currentColor"></path><path d="M20.5 11a2.5 2.5 0 1 0 2.5 2.5a2.48 2.48 0 0 0-2.5-2.5z" fill="currentColor"></path></svg>
							blame
						</a><a class="my-1 mr-4 flex items-center hover:underline text-green-600 dark:text-gray-300" href="/TheBloke/Mistral-7B-v0.1-GGUF/edit/main/README.md"><svg class="mr-1.5" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32"><path d="M2 26h28v2H2z" fill="currentColor"></path><path d="M25.4 9c.8-.8.8-2 0-2.8l-3.6-3.6c-.8-.8-2-.8-2.8 0l-15 15V24h6.4l15-15zm-5-5L24 7.6l-3 3L17.4 7l3-3zM6 22v-3.6l10-10l3.6 3.6l-10 10H6z" fill="currentColor"></path></svg>
							contribute
						</a><a class="my-1 mr-4 flex items-center hover:underline " href="/TheBloke/Mistral-7B-v0.1-GGUF/delete/main/README.md"><svg class="mr-1.5" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32"><path d="M12 12h2v12h-2z" fill="currentColor"></path><path d="M18 12h2v12h-2z" fill="currentColor"></path><path d="M4 6v2h2v20a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V8h2V6zm4 22V8h16v20z" fill="currentColor"></path><path d="M12 2h8v2h-8z" fill="currentColor"></path></svg>
							delete
						</a>
				<div class="mr-4 flex items-center text-gray-400"><svg class="text-gray-300 text-sm mr-1.5 -translate-y-px" width="1em" height="1em" viewBox="0 0 22 28" fill="none" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" clip-rule="evenodd" d="M15.3634 10.3639C15.8486 10.8491 15.8486 11.6357 15.3634 12.1209L10.9292 16.5551C10.6058 16.8785 10.0814 16.8785 9.7579 16.5551L7.03051 13.8277C6.54532 13.3425 6.54532 12.5558 7.03051 12.0707C7.51569 11.5855 8.30234 11.5855 8.78752 12.0707L9.7579 13.041C10.0814 13.3645 10.6058 13.3645 10.9292 13.041L13.6064 10.3639C14.0916 9.8787 14.8782 9.8787 15.3634 10.3639Z" fill="currentColor"></path><path fill-rule="evenodd" clip-rule="evenodd" d="M10.6666 27.12C4.93329 25.28 0 19.2267 0 12.7867V6.52001C0 5.40001 0.693334 4.41334 1.73333 4.01334L9.73333 1.01334C10.3333 0.786673 11 0.786673 11.6 1.02667L19.6 4.02667C20.1083 4.21658 20.5465 4.55701 20.8562 5.00252C21.1659 5.44803 21.3324 5.97742 21.3333 6.52001V12.7867C21.3333 19.24 16.4 25.28 10.6666 27.12Z" fill="currentColor" fill-opacity="0.22"></path><path d="M10.0845 1.94967L10.0867 1.94881C10.4587 1.8083 10.8666 1.81036 11.2286 1.95515L11.2387 1.95919L11.2489 1.963L19.2489 4.963L19.25 4.96342C19.5677 5.08211 19.8416 5.29488 20.0351 5.57333C20.2285 5.85151 20.3326 6.18203 20.3333 6.52082C20.3333 6.52113 20.3333 6.52144 20.3333 6.52176L20.3333 12.7867C20.3333 18.6535 15.8922 24.2319 10.6666 26.0652C5.44153 24.2316 1 18.6409 1 12.7867V6.52001C1 5.82357 1.42893 5.20343 2.08883 4.94803L10.0845 1.94967Z" stroke="currentColor" stroke-opacity="0.30" stroke-width="2"></path></svg>

							No virus
						</div>
				
				<div class="flex items-center gap-x-3 dark:text-gray-300 sm:ml-auto">
					17.2 kB</div></div>

			<div class="relative min-h-[100px] rounded-b-lg border border-t-0 leading-tight dark:border-gray-800 dark:bg-gray-925">
				
						<div class="py-4 px-4 sm:px-6 prose hf-sanitized hf-sanitized-JINHjPatfKEr4atO0xKen"><div class="not-prose -mx-6 -mt-4 mb-8 max-h-[300px] min-w-full overflow-auto border-b bg-gradient-to-t from-gray-50 px-6 pb-5 pt-4 font-mono text-xs transition-all dark:from-gray-900 dark:to-gray-950"><div class="mb-2 inline-block rounded-lg border px-2 py-1 font-mono text-xs leading-none">metadata</div>
			<pre><!-- HTML_TAG_START --><span class="hljs-attr">base_model:</span> <span class="hljs-string">mistralai/Mistral-7B-v0.1</span>
<span class="hljs-attr">inference:</span> <span class="hljs-literal">false</span>
<span class="hljs-attr">license:</span> <span class="hljs-string">apache-2.0</span>
<span class="hljs-attr">model_creator:</span> <span class="hljs-string">Mistral</span> <span class="hljs-string">AI</span>
<span class="hljs-attr">model_name:</span> <span class="hljs-string">Mistral</span> <span class="hljs-string">7B</span> <span class="hljs-string">v0.1</span>
<span class="hljs-attr">model_type:</span> <span class="hljs-string">mistral</span>
<span class="hljs-attr">pipeline_tag:</span> <span class="hljs-string">text-generation</span>
<span class="hljs-attr">prompt_template:</span> <span class="hljs-string">|</span>
<span class="hljs-string">  {prompt}</span>
<span class="hljs-string"></span><span class="hljs-attr">quantized_by:</span> <span class="hljs-string">TheBloke</span>
<span class="hljs-attr">tags:</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">pretrained</span>
<!-- HTML_TAG_END --></pre></div>
	<!-- HTML_TAG_START --><div style="width: auto; margin-left: auto; margin-right: auto">
<img style="width: 100%; min-width: 400px; display: block; margin: auto;" alt="TheBlokeAI" src="https://i.imgur.com/EBdldam.jpg">
</div>
<div style="display: flex; justify-content: space-between; width: 100%;">
    <div style="display: flex; flex-direction: column; align-items: flex-start;">
        <p style="margin-top: 0.5em; margin-bottom: 0em;"><a rel="nofollow" href="https://discord.gg/theblokeai">Chat &amp; support: TheBloke's Discord server</a></p>
    </div>
    <div style="display: flex; flex-direction: column; align-items: flex-end;">
        <p style="margin-top: 0.5em; margin-bottom: 0em;"><a rel="nofollow" href="https://www.patreon.com/TheBlokeAI">Want to contribute? TheBloke's Patreon page</a></p>
    </div>
</div>
<div style="text-align:center; margin-top: 0em; margin-bottom: 0em"><p style="margin-top: 0.25em; margin-bottom: 0em;">TheBloke's LLM work is generously supported by a grant from <a rel="nofollow" href="https://a16z.com">andreessen horowitz (a16z)</a></p></div>
<hr style="margin-top: 1.0em; margin-bottom: 1.0em;">


<h1 class="relative group flex items-center">
	<a rel="nofollow" href="#mistral-7b-v01---gguf" class="block pr-1.5 text-lg md:absolute md:p-1.5 md:opacity-0 md:group-hover:opacity-100 md:right-full" id="mistral-7b-v01---gguf">
		<span class="header-link"><svg viewBox="0 0 256 256" preserveAspectRatio="xMidYMid meet" height="1em" width="1em" role="img" aria-hidden="true" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-black dark:hover:text-gray-200 w-4"><path fill="currentColor" d="M167.594 88.393a8.001 8.001 0 0 1 0 11.314l-67.882 67.882a8 8 0 1 1-11.314-11.315l67.882-67.881a8.003 8.003 0 0 1 11.314 0zm-28.287 84.86l-28.284 28.284a40 40 0 0 1-56.567-56.567l28.284-28.284a8 8 0 0 0-11.315-11.315l-28.284 28.284a56 56 0 0 0 79.196 79.197l28.285-28.285a8 8 0 1 0-11.315-11.314zM212.852 43.14a56.002 56.002 0 0 0-79.196 0l-28.284 28.284a8 8 0 1 0 11.314 11.314l28.284-28.284a40 40 0 0 1 56.568 56.567l-28.285 28.285a8 8 0 0 0 11.315 11.314l28.284-28.284a56.065 56.065 0 0 0 0-79.196z"></path></svg></span>
	</a>
	<span>
		Mistral 7B v0.1 - GGUF
	</span>
</h1>
<ul>
<li>Model creator: <a rel="nofollow" href="https://huggingface.co/mistralai">Mistral AI</a></li>
<li>Original model: <a rel="nofollow" href="https://huggingface.co/mistralai/Mistral-7B-v0.1">Mistral 7B v0.1</a></li>
</ul>

<h2 class="relative group flex items-center">
	<a rel="nofollow" href="#description" class="block pr-1.5 text-lg md:absolute md:p-1.5 md:opacity-0 md:group-hover:opacity-100 md:right-full" id="description">
		<span class="header-link"><svg viewBox="0 0 256 256" preserveAspectRatio="xMidYMid meet" height="1em" width="1em" role="img" aria-hidden="true" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-black dark:hover:text-gray-200 w-4"><path fill="currentColor" d="M167.594 88.393a8.001 8.001 0 0 1 0 11.314l-67.882 67.882a8 8 0 1 1-11.314-11.315l67.882-67.881a8.003 8.003 0 0 1 11.314 0zm-28.287 84.86l-28.284 28.284a40 40 0 0 1-56.567-56.567l28.284-28.284a8 8 0 0 0-11.315-11.315l-28.284 28.284a56 56 0 0 0 79.196 79.197l28.285-28.285a8 8 0 1 0-11.315-11.314zM212.852 43.14a56.002 56.002 0 0 0-79.196 0l-28.284 28.284a8 8 0 1 0 11.314 11.314l28.284-28.284a40 40 0 0 1 56.568 56.567l-28.285 28.285a8 8 0 0 0 11.315 11.314l28.284-28.284a56.065 56.065 0 0 0 0-79.196z"></path></svg></span>
	</a>
	<span>
		Description
	</span>
</h2>
<p>This repo contains GGUF format model files for <a rel="nofollow" href="https://huggingface.co/mistralai/Mistral-7B-v0.1">Mistral AI's Mistral 7B v0.1</a>.</p>


<h3 class="relative group flex items-center">
	<a rel="nofollow" href="#about-gguf" class="block pr-1.5 text-lg md:absolute md:p-1.5 md:opacity-0 md:group-hover:opacity-100 md:right-full" id="about-gguf">
		<span class="header-link"><svg viewBox="0 0 256 256" preserveAspectRatio="xMidYMid meet" height="1em" width="1em" role="img" aria-hidden="true" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-black dark:hover:text-gray-200 w-4"><path fill="currentColor" d="M167.594 88.393a8.001 8.001 0 0 1 0 11.314l-67.882 67.882a8 8 0 1 1-11.314-11.315l67.882-67.881a8.003 8.003 0 0 1 11.314 0zm-28.287 84.86l-28.284 28.284a40 40 0 0 1-56.567-56.567l28.284-28.284a8 8 0 0 0-11.315-11.315l-28.284 28.284a56 56 0 0 0 79.196 79.197l28.285-28.285a8 8 0 1 0-11.315-11.314zM212.852 43.14a56.002 56.002 0 0 0-79.196 0l-28.284 28.284a8 8 0 1 0 11.314 11.314l28.284-28.284a40 40 0 0 1 56.568 56.567l-28.285 28.285a8 8 0 0 0 11.315 11.314l28.284-28.284a56.065 56.065 0 0 0 0-79.196z"></path></svg></span>
	</a>
	<span>
		About GGUF
	</span>
</h3>
<p>GGUF is a new format introduced by the llama.cpp team on August 21st 2023. It is a replacement for GGML, which is no longer supported by llama.cpp.</p>
<p>Here is an incomplate list of clients and libraries that are known to support GGUF:</p>
<ul>
<li><a rel="nofollow" href="https://github.com/ggerganov/llama.cpp">llama.cpp</a>. The source project for GGUF. Offers a CLI and a server option.</li>
<li><a rel="nofollow" href="https://github.com/oobabooga/text-generation-webui">text-generation-webui</a>, the most widely used web UI, with many features and powerful extensions. Supports GPU acceleration.</li>
<li><a rel="nofollow" href="https://github.com/LostRuins/koboldcpp">KoboldCpp</a>, a fully featured web UI, with GPU accel across all platforms and GPU architectures. Especially good for story telling.</li>
<li><a rel="nofollow" href="https://lmstudio.ai/">LM Studio</a>, an easy-to-use and powerful local GUI for Windows and macOS (Silicon), with GPU acceleration.</li>
<li><a rel="nofollow" href="https://github.com/ParisNeo/lollms-webui">LoLLMS Web UI</a>, a great web UI with many interesting and unique features, including a full model library for easy model selection.</li>
<li><a rel="nofollow" href="https://faraday.dev/">Faraday.dev</a>, an attractive and easy to use character-based chat GUI for Windows and macOS (both Silicon and Intel), with GPU acceleration.</li>
<li><a rel="nofollow" href="https://github.com/marella/ctransformers">ctransformers</a>, a Python library with GPU accel, LangChain support, and OpenAI-compatible AI server.</li>
<li><a rel="nofollow" href="https://github.com/abetlen/llama-cpp-python">llama-cpp-python</a>, a Python library with GPU accel, LangChain support, and OpenAI-compatible API server.</li>
<li><a rel="nofollow" href="https://github.com/huggingface/candle">candle</a>, a Rust ML framework with a focus on performance, including GPU support, and ease of use.</li>
</ul>


<h2 class="relative group flex items-center">
	<a rel="nofollow" href="#repositories-available" class="block pr-1.5 text-lg md:absolute md:p-1.5 md:opacity-0 md:group-hover:opacity-100 md:right-full" id="repositories-available">
		<span class="header-link"><svg viewBox="0 0 256 256" preserveAspectRatio="xMidYMid meet" height="1em" width="1em" role="img" aria-hidden="true" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-black dark:hover:text-gray-200 w-4"><path fill="currentColor" d="M167.594 88.393a8.001 8.001 0 0 1 0 11.314l-67.882 67.882a8 8 0 1 1-11.314-11.315l67.882-67.881a8.003 8.003 0 0 1 11.314 0zm-28.287 84.86l-28.284 28.284a40 40 0 0 1-56.567-56.567l28.284-28.284a8 8 0 0 0-11.315-11.315l-28.284 28.284a56 56 0 0 0 79.196 79.197l28.285-28.285a8 8 0 1 0-11.315-11.314zM212.852 43.14a56.002 56.002 0 0 0-79.196 0l-28.284 28.284a8 8 0 1 0 11.314 11.314l28.284-28.284a40 40 0 0 1 56.568 56.567l-28.285 28.285a8 8 0 0 0 11.315 11.314l28.284-28.284a56.065 56.065 0 0 0 0-79.196z"></path></svg></span>
	</a>
	<span>
		Repositories available
	</span>
</h2>
<ul>
<li><a rel="nofollow" href="https://huggingface.co/TheBloke/Mistral-7B-v0.1-AWQ">AWQ model(s) for GPU inference.</a></li>
<li><a rel="nofollow" href="https://huggingface.co/TheBloke/Mistral-7B-v0.1-GPTQ">GPTQ models for GPU inference, with multiple quantisation parameter options.</a></li>
<li><a rel="nofollow" href="https://huggingface.co/TheBloke/Mistral-7B-v0.1-GGUF">2, 3, 4, 5, 6 and 8-bit GGUF models for CPU+GPU inference</a></li>
<li><a rel="nofollow" href="https://huggingface.co/mistralai/Mistral-7B-v0.1">Mistral AI's original unquantised fp16 model in pytorch format, for GPU inference and for further conversions</a></li>
</ul>

<h2 class="relative group flex items-center">
	<a rel="nofollow" href="#prompt-template-none" class="block pr-1.5 text-lg md:absolute md:p-1.5 md:opacity-0 md:group-hover:opacity-100 md:right-full" id="prompt-template-none">
		<span class="header-link"><svg viewBox="0 0 256 256" preserveAspectRatio="xMidYMid meet" height="1em" width="1em" role="img" aria-hidden="true" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-black dark:hover:text-gray-200 w-4"><path fill="currentColor" d="M167.594 88.393a8.001 8.001 0 0 1 0 11.314l-67.882 67.882a8 8 0 1 1-11.314-11.315l67.882-67.881a8.003 8.003 0 0 1 11.314 0zm-28.287 84.86l-28.284 28.284a40 40 0 0 1-56.567-56.567l28.284-28.284a8 8 0 0 0-11.315-11.315l-28.284 28.284a56 56 0 0 0 79.196 79.197l28.285-28.285a8 8 0 1 0-11.315-11.314zM212.852 43.14a56.002 56.002 0 0 0-79.196 0l-28.284 28.284a8 8 0 1 0 11.314 11.314l28.284-28.284a40 40 0 0 1 56.568 56.567l-28.285 28.285a8 8 0 0 0 11.315 11.314l28.284-28.284a56.065 56.065 0 0 0 0-79.196z"></path></svg></span>
	</a>
	<span>
		Prompt template: None
	</span>
</h2>
<pre><code>{prompt}
</code></pre>




<h2 class="relative group flex items-center">
	<a rel="nofollow" href="#compatibility" class="block pr-1.5 text-lg md:absolute md:p-1.5 md:opacity-0 md:group-hover:opacity-100 md:right-full" id="compatibility">
		<span class="header-link"><svg viewBox="0 0 256 256" preserveAspectRatio="xMidYMid meet" height="1em" width="1em" role="img" aria-hidden="true" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-black dark:hover:text-gray-200 w-4"><path fill="currentColor" d="M167.594 88.393a8.001 8.001 0 0 1 0 11.314l-67.882 67.882a8 8 0 1 1-11.314-11.315l67.882-67.881a8.003 8.003 0 0 1 11.314 0zm-28.287 84.86l-28.284 28.284a40 40 0 0 1-56.567-56.567l28.284-28.284a8 8 0 0 0-11.315-11.315l-28.284 28.284a56 56 0 0 0 79.196 79.197l28.285-28.285a8 8 0 1 0-11.315-11.314zM212.852 43.14a56.002 56.002 0 0 0-79.196 0l-28.284 28.284a8 8 0 1 0 11.314 11.314l28.284-28.284a40 40 0 0 1 56.568 56.567l-28.285 28.285a8 8 0 0 0 11.315 11.314l28.284-28.284a56.065 56.065 0 0 0 0-79.196z"></path></svg></span>
	</a>
	<span>
		Compatibility
	</span>
</h2>
<p>These quantised GGUFv2 files are compatible with llama.cpp from August 27th onwards, as of commit <a rel="nofollow" href="https://github.com/ggerganov/llama.cpp/commit/d0cee0d36d5be95a0d9088b674dbb27354107221">d0cee0d</a></p>
<p>They are also compatible with many third party UIs and libraries - please see the list at the top of this README.</p>
<p>Sequence length note: The model will work at sequence lengths of 4096, or lower. GGUF does not yet have support for the new sliding window sequence length mode, so longer sequence lengths are not supported.</p>
<h2 class="relative group flex items-center">
	<a rel="nofollow" href="#explanation-of-quantisation-methods" class="block pr-1.5 text-lg md:absolute md:p-1.5 md:opacity-0 md:group-hover:opacity-100 md:right-full" id="explanation-of-quantisation-methods">
		<span class="header-link"><svg viewBox="0 0 256 256" preserveAspectRatio="xMidYMid meet" height="1em" width="1em" role="img" aria-hidden="true" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-black dark:hover:text-gray-200 w-4"><path fill="currentColor" d="M167.594 88.393a8.001 8.001 0 0 1 0 11.314l-67.882 67.882a8 8 0 1 1-11.314-11.315l67.882-67.881a8.003 8.003 0 0 1 11.314 0zm-28.287 84.86l-28.284 28.284a40 40 0 0 1-56.567-56.567l28.284-28.284a8 8 0 0 0-11.315-11.315l-28.284 28.284a56 56 0 0 0 79.196 79.197l28.285-28.285a8 8 0 1 0-11.315-11.314zM212.852 43.14a56.002 56.002 0 0 0-79.196 0l-28.284 28.284a8 8 0 1 0 11.314 11.314l28.284-28.284a40 40 0 0 1 56.568 56.567l-28.285 28.285a8 8 0 0 0 11.315 11.314l28.284-28.284a56.065 56.065 0 0 0 0-79.196z"></path></svg></span>
	</a>
	<span>
		Explanation of quantisation methods
	</span>
</h2>
<details>
  <summary>Click to see details</summary>

<p>The new methods available are:</p>
<ul>
<li>GGML_TYPE_Q2_K - "type-1" 2-bit quantization in super-blocks containing 16 blocks, each block having 16 weight. Block scales and mins are quantized with 4 bits. This ends up effectively using 2.5625 bits per weight (bpw)</li>
<li>GGML_TYPE_Q3_K - "type-0" 3-bit quantization in super-blocks containing 16 blocks, each block having 16 weights. Scales are quantized with 6 bits. This end up using 3.4375 bpw.</li>
<li>GGML_TYPE_Q4_K - "type-1" 4-bit quantization in super-blocks containing 8 blocks, each block having 32 weights. Scales and mins are quantized with 6 bits. This ends up using 4.5 bpw.</li>
<li>GGML_TYPE_Q5_K - "type-1" 5-bit quantization. Same super-block structure as GGML_TYPE_Q4_K resulting in 5.5 bpw</li>
<li>GGML_TYPE_Q6_K - "type-0" 6-bit quantization. Super-blocks with 16 blocks, each block having 16 weights. Scales are quantized with 8 bits. This ends up using 6.5625 bpw</li>
</ul>
<p>Refer to the Provided Files table below to see what files use which methods, and how.</p>
</details>



<h2 class="relative group flex items-center">
	<a rel="nofollow" href="#provided-files" class="block pr-1.5 text-lg md:absolute md:p-1.5 md:opacity-0 md:group-hover:opacity-100 md:right-full" id="provided-files">
		<span class="header-link"><svg viewBox="0 0 256 256" preserveAspectRatio="xMidYMid meet" height="1em" width="1em" role="img" aria-hidden="true" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-black dark:hover:text-gray-200 w-4"><path fill="currentColor" d="M167.594 88.393a8.001 8.001 0 0 1 0 11.314l-67.882 67.882a8 8 0 1 1-11.314-11.315l67.882-67.881a8.003 8.003 0 0 1 11.314 0zm-28.287 84.86l-28.284 28.284a40 40 0 0 1-56.567-56.567l28.284-28.284a8 8 0 0 0-11.315-11.315l-28.284 28.284a56 56 0 0 0 79.196 79.197l28.285-28.285a8 8 0 1 0-11.315-11.314zM212.852 43.14a56.002 56.002 0 0 0-79.196 0l-28.284 28.284a8 8 0 1 0 11.314 11.314l28.284-28.284a40 40 0 0 1 56.568 56.567l-28.285 28.285a8 8 0 0 0 11.315 11.314l28.284-28.284a56.065 56.065 0 0 0 0-79.196z"></path></svg></span>
	</a>
	<span>
		Provided files
	</span>
</h2>
<div class="max-w-full overflow-auto">
	<table>
		<thead><tr>
<th>Name</th>
<th>Quant method</th>
<th>Bits</th>
<th>Size</th>
<th>Max RAM required</th>
<th>Use case</th>
</tr>

		</thead><tbody><tr>
<td><a rel="nofollow" href="https://huggingface.co/TheBloke/Mistral-7B-v0.1-GGUF/blob/main/mistral-7b-v0.1.Q2_K.gguf">mistral-7b-v0.1.Q2_K.gguf</a></td>
<td>Q2_K</td>
<td>2</td>
<td>3.08 GB</td>
<td>5.58 GB</td>
<td>smallest, significant quality loss - not recommended for most purposes</td>
</tr>
<tr>
<td><a rel="nofollow" href="https://huggingface.co/TheBloke/Mistral-7B-v0.1-GGUF/blob/main/mistral-7b-v0.1.Q3_K_S.gguf">mistral-7b-v0.1.Q3_K_S.gguf</a></td>
<td>Q3_K_S</td>
<td>3</td>
<td>3.16 GB</td>
<td>5.66 GB</td>
<td>very small, high quality loss</td>
</tr>
<tr>
<td><a rel="nofollow" href="https://huggingface.co/TheBloke/Mistral-7B-v0.1-GGUF/blob/main/mistral-7b-v0.1.Q3_K_M.gguf">mistral-7b-v0.1.Q3_K_M.gguf</a></td>
<td>Q3_K_M</td>
<td>3</td>
<td>3.52 GB</td>
<td>6.02 GB</td>
<td>very small, high quality loss</td>
</tr>
<tr>
<td><a rel="nofollow" href="https://huggingface.co/TheBloke/Mistral-7B-v0.1-GGUF/blob/main/mistral-7b-v0.1.Q3_K_L.gguf">mistral-7b-v0.1.Q3_K_L.gguf</a></td>
<td>Q3_K_L</td>
<td>3</td>
<td>3.82 GB</td>
<td>6.32 GB</td>
<td>small, substantial quality loss</td>
</tr>
<tr>
<td><a rel="nofollow" href="https://huggingface.co/TheBloke/Mistral-7B-v0.1-GGUF/blob/main/mistral-7b-v0.1.Q4_0.gguf">mistral-7b-v0.1.Q4_0.gguf</a></td>
<td>Q4_0</td>
<td>4</td>
<td>4.11 GB</td>
<td>6.61 GB</td>
<td>legacy; small, very high quality loss - prefer using Q3_K_M</td>
</tr>
<tr>
<td><a rel="nofollow" href="https://huggingface.co/TheBloke/Mistral-7B-v0.1-GGUF/blob/main/mistral-7b-v0.1.Q4_K_S.gguf">mistral-7b-v0.1.Q4_K_S.gguf</a></td>
<td>Q4_K_S</td>
<td>4</td>
<td>4.14 GB</td>
<td>6.64 GB</td>
<td>small, greater quality loss</td>
</tr>
<tr>
<td><a rel="nofollow" href="https://huggingface.co/TheBloke/Mistral-7B-v0.1-GGUF/blob/main/mistral-7b-v0.1.Q4_K_M.gguf">mistral-7b-v0.1.Q4_K_M.gguf</a></td>
<td>Q4_K_M</td>
<td>4</td>
<td>4.37 GB</td>
<td>6.87 GB</td>
<td>medium, balanced quality - recommended</td>
</tr>
<tr>
<td><a rel="nofollow" href="https://huggingface.co/TheBloke/Mistral-7B-v0.1-GGUF/blob/main/mistral-7b-v0.1.Q5_0.gguf">mistral-7b-v0.1.Q5_0.gguf</a></td>
<td>Q5_0</td>
<td>5</td>
<td>5.00 GB</td>
<td>7.50 GB</td>
<td>legacy; medium, balanced quality - prefer using Q4_K_M</td>
</tr>
<tr>
<td><a rel="nofollow" href="https://huggingface.co/TheBloke/Mistral-7B-v0.1-GGUF/blob/main/mistral-7b-v0.1.Q5_K_S.gguf">mistral-7b-v0.1.Q5_K_S.gguf</a></td>
<td>Q5_K_S</td>
<td>5</td>
<td>5.00 GB</td>
<td>7.50 GB</td>
<td>large, low quality loss - recommended</td>
</tr>
<tr>
<td><a rel="nofollow" href="https://huggingface.co/TheBloke/Mistral-7B-v0.1-GGUF/blob/main/mistral-7b-v0.1.Q5_K_M.gguf">mistral-7b-v0.1.Q5_K_M.gguf</a></td>
<td>Q5_K_M</td>
<td>5</td>
<td>5.13 GB</td>
<td>7.63 GB</td>
<td>large, very low quality loss - recommended</td>
</tr>
<tr>
<td><a rel="nofollow" href="https://huggingface.co/TheBloke/Mistral-7B-v0.1-GGUF/blob/main/mistral-7b-v0.1.Q6_K.gguf">mistral-7b-v0.1.Q6_K.gguf</a></td>
<td>Q6_K</td>
<td>6</td>
<td>5.94 GB</td>
<td>8.44 GB</td>
<td>very large, extremely low quality loss</td>
</tr>
<tr>
<td><a rel="nofollow" href="https://huggingface.co/TheBloke/Mistral-7B-v0.1-GGUF/blob/main/mistral-7b-v0.1.Q8_0.gguf">mistral-7b-v0.1.Q8_0.gguf</a></td>
<td>Q8_0</td>
<td>8</td>
<td>7.70 GB</td>
<td>10.20 GB</td>
<td>very large, extremely low quality loss - not recommended</td>
</tr>
</tbody>
	</table>
</div>
<p><strong>Note</strong>: the above RAM figures assume no GPU offloading. If layers are offloaded to the GPU, this will reduce RAM usage and use VRAM instead.</p>



<h2 class="relative group flex items-center">
	<a rel="nofollow" href="#how-to-download-gguf-files" class="block pr-1.5 text-lg md:absolute md:p-1.5 md:opacity-0 md:group-hover:opacity-100 md:right-full" id="how-to-download-gguf-files">
		<span class="header-link"><svg viewBox="0 0 256 256" preserveAspectRatio="xMidYMid meet" height="1em" width="1em" role="img" aria-hidden="true" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-black dark:hover:text-gray-200 w-4"><path fill="currentColor" d="M167.594 88.393a8.001 8.001 0 0 1 0 11.314l-67.882 67.882a8 8 0 1 1-11.314-11.315l67.882-67.881a8.003 8.003 0 0 1 11.314 0zm-28.287 84.86l-28.284 28.284a40 40 0 0 1-56.567-56.567l28.284-28.284a8 8 0 0 0-11.315-11.315l-28.284 28.284a56 56 0 0 0 79.196 79.197l28.285-28.285a8 8 0 1 0-11.315-11.314zM212.852 43.14a56.002 56.002 0 0 0-79.196 0l-28.284 28.284a8 8 0 1 0 11.314 11.314l28.284-28.284a40 40 0 0 1 56.568 56.567l-28.285 28.285a8 8 0 0 0 11.315 11.314l28.284-28.284a56.065 56.065 0 0 0 0-79.196z"></path></svg></span>
	</a>
	<span>
		How to download GGUF files
	</span>
</h2>
<p><strong>Note for manual downloaders:</strong> You almost never want to clone the entire repo! Multiple different quantisation formats are provided, and most users only want to pick and download a single file.</p>
<p>The following clients/libraries will automatically download models for you, providing a list of available models to choose from:</p>
<ul>
<li>LM Studio</li>
<li>LoLLMS Web UI</li>
<li>Faraday.dev</li>
</ul>
<h3 class="relative group flex items-center">
	<a rel="nofollow" href="#in-text-generation-webui" class="block pr-1.5 text-lg md:absolute md:p-1.5 md:opacity-0 md:group-hover:opacity-100 md:right-full" id="in-text-generation-webui">
		<span class="header-link"><svg viewBox="0 0 256 256" preserveAspectRatio="xMidYMid meet" height="1em" width="1em" role="img" aria-hidden="true" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-black dark:hover:text-gray-200 w-4"><path fill="currentColor" d="M167.594 88.393a8.001 8.001 0 0 1 0 11.314l-67.882 67.882a8 8 0 1 1-11.314-11.315l67.882-67.881a8.003 8.003 0 0 1 11.314 0zm-28.287 84.86l-28.284 28.284a40 40 0 0 1-56.567-56.567l28.284-28.284a8 8 0 0 0-11.315-11.315l-28.284 28.284a56 56 0 0 0 79.196 79.197l28.285-28.285a8 8 0 1 0-11.315-11.314zM212.852 43.14a56.002 56.002 0 0 0-79.196 0l-28.284 28.284a8 8 0 1 0 11.314 11.314l28.284-28.284a40 40 0 0 1 56.568 56.567l-28.285 28.285a8 8 0 0 0 11.315 11.314l28.284-28.284a56.065 56.065 0 0 0 0-79.196z"></path></svg></span>
	</a>
	<span>
		In <code>text-generation-webui</code>
	</span>
</h3>
<p>Under Download Model, you can enter the model repo: TheBloke/Mistral-7B-v0.1-GGUF and below it, a specific filename to download, such as: mistral-7b-v0.1.Q4_K_M.gguf.</p>
<p>Then click Download.</p>
<h3 class="relative group flex items-center">
	<a rel="nofollow" href="#on-the-command-line-including-multiple-files-at-once" class="block pr-1.5 text-lg md:absolute md:p-1.5 md:opacity-0 md:group-hover:opacity-100 md:right-full" id="on-the-command-line-including-multiple-files-at-once">
		<span class="header-link"><svg viewBox="0 0 256 256" preserveAspectRatio="xMidYMid meet" height="1em" width="1em" role="img" aria-hidden="true" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-black dark:hover:text-gray-200 w-4"><path fill="currentColor" d="M167.594 88.393a8.001 8.001 0 0 1 0 11.314l-67.882 67.882a8 8 0 1 1-11.314-11.315l67.882-67.881a8.003 8.003 0 0 1 11.314 0zm-28.287 84.86l-28.284 28.284a40 40 0 0 1-56.567-56.567l28.284-28.284a8 8 0 0 0-11.315-11.315l-28.284 28.284a56 56 0 0 0 79.196 79.197l28.285-28.285a8 8 0 1 0-11.315-11.314zM212.852 43.14a56.002 56.002 0 0 0-79.196 0l-28.284 28.284a8 8 0 1 0 11.314 11.314l28.284-28.284a40 40 0 0 1 56.568 56.567l-28.285 28.285a8 8 0 0 0 11.315 11.314l28.284-28.284a56.065 56.065 0 0 0 0-79.196z"></path></svg></span>
	</a>
	<span>
		On the command line, including multiple files at once
	</span>
</h3>
<p>I recommend using the <code>huggingface-hub</code> Python library:</p>
<pre><code class="language-shell">pip3 install huggingface-hub
</code></pre>
<p>Then you can download any individual model file to the current directory, at high speed, with a command like this:</p>
<pre><code class="language-shell">huggingface-cli download TheBloke/Mistral-7B-v0.1-GGUF mistral-7b-v0.1.Q4_K_M.gguf --local-dir . --local-dir-use-symlinks False
</code></pre>
<details>
  <summary>More advanced huggingface-cli download usage</summary>

<p>You can also download multiple files at once with a pattern:</p>
<pre><code class="language-shell">huggingface-cli download TheBloke/Mistral-7B-v0.1-GGUF --local-dir . --local-dir-use-symlinks False --include='*Q4_K*gguf'
</code></pre>
<p>For more documentation on downloading with <code>huggingface-cli</code>, please see: <a rel="nofollow" href="https://huggingface.co/docs/huggingface_hub/guides/download#download-from-the-cli">HF -&gt; Hub Python Library -&gt; Download files -&gt; Download from the CLI</a>.</p>
<p>To accelerate downloads on fast connections (1Gbit/s or higher), install <code>hf_transfer</code>:</p>
<pre><code class="language-shell">pip3 install hf_transfer
</code></pre>
<p>And set environment variable <code>HF_HUB_ENABLE_HF_TRANSFER</code> to <code>1</code>:</p>
<pre><code class="language-shell">HF_HUB_ENABLE_HF_TRANSFER=1 huggingface-cli download TheBloke/Mistral-7B-v0.1-GGUF mistral-7b-v0.1.Q4_K_M.gguf --local-dir . --local-dir-use-symlinks False
</code></pre>
<p>Windows Command Line users: You can set the environment variable by running <code>set HF_HUB_ENABLE_HF_TRANSFER=1</code> before the download command.</p>
</details>



<h2 class="relative group flex items-center">
	<a rel="nofollow" href="#example-llamacpp-command" class="block pr-1.5 text-lg md:absolute md:p-1.5 md:opacity-0 md:group-hover:opacity-100 md:right-full" id="example-llamacpp-command">
		<span class="header-link"><svg viewBox="0 0 256 256" preserveAspectRatio="xMidYMid meet" height="1em" width="1em" role="img" aria-hidden="true" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-black dark:hover:text-gray-200 w-4"><path fill="currentColor" d="M167.594 88.393a8.001 8.001 0 0 1 0 11.314l-67.882 67.882a8 8 0 1 1-11.314-11.315l67.882-67.881a8.003 8.003 0 0 1 11.314 0zm-28.287 84.86l-28.284 28.284a40 40 0 0 1-56.567-56.567l28.284-28.284a8 8 0 0 0-11.315-11.315l-28.284 28.284a56 56 0 0 0 79.196 79.197l28.285-28.285a8 8 0 1 0-11.315-11.314zM212.852 43.14a56.002 56.002 0 0 0-79.196 0l-28.284 28.284a8 8 0 1 0 11.314 11.314l28.284-28.284a40 40 0 0 1 56.568 56.567l-28.285 28.285a8 8 0 0 0 11.315 11.314l28.284-28.284a56.065 56.065 0 0 0 0-79.196z"></path></svg></span>
	</a>
	<span>
		Example <code>llama.cpp</code> command
	</span>
</h2>
<p>Make sure you are using <code>llama.cpp</code> from commit <a rel="nofollow" href="https://github.com/ggerganov/llama.cpp/commit/d0cee0d36d5be95a0d9088b674dbb27354107221">d0cee0d</a> or later.</p>
<pre><code class="language-shell">./main -ngl 32 -m mistral-7b-v0.1.Q4_K_M.gguf --color -c 4096 --temp 0.7 --repeat_penalty 1.1 -n -1 -p "{prompt}"
</code></pre>
<p>Change <code>-ngl 32</code> to the number of layers to offload to GPU. Remove it if you don't have GPU acceleration.</p>
<p>Sequence length can be 4096 or lower. Mistral's sliding window sequence length is not yet supported in llama.cpp, so sequence lengths longer than 4096 are not supported.</p>
<p>If you want to have a chat-style conversation, replace the <code>-p &lt;PROMPT&gt;</code> argument with <code>-i -ins</code></p>
<p>For other parameters and how to use them, please refer to <a rel="nofollow" href="https://github.com/ggerganov/llama.cpp/blob/master/examples/main/README.md">the llama.cpp documentation</a></p>
<h2 class="relative group flex items-center">
	<a rel="nofollow" href="#how-to-run-in-text-generation-webui" class="block pr-1.5 text-lg md:absolute md:p-1.5 md:opacity-0 md:group-hover:opacity-100 md:right-full" id="how-to-run-in-text-generation-webui">
		<span class="header-link"><svg viewBox="0 0 256 256" preserveAspectRatio="xMidYMid meet" height="1em" width="1em" role="img" aria-hidden="true" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-black dark:hover:text-gray-200 w-4"><path fill="currentColor" d="M167.594 88.393a8.001 8.001 0 0 1 0 11.314l-67.882 67.882a8 8 0 1 1-11.314-11.315l67.882-67.881a8.003 8.003 0 0 1 11.314 0zm-28.287 84.86l-28.284 28.284a40 40 0 0 1-56.567-56.567l28.284-28.284a8 8 0 0 0-11.315-11.315l-28.284 28.284a56 56 0 0 0 79.196 79.197l28.285-28.285a8 8 0 1 0-11.315-11.314zM212.852 43.14a56.002 56.002 0 0 0-79.196 0l-28.284 28.284a8 8 0 1 0 11.314 11.314l28.284-28.284a40 40 0 0 1 56.568 56.567l-28.285 28.285a8 8 0 0 0 11.315 11.314l28.284-28.284a56.065 56.065 0 0 0 0-79.196z"></path></svg></span>
	</a>
	<span>
		How to run in <code>text-generation-webui</code>
	</span>
</h2>
<p>Further instructions here: <a rel="nofollow" href="https://github.com/oobabooga/text-generation-webui/blob/main/docs/llama.cpp.md">text-generation-webui/docs/llama.cpp.md</a>.</p>
<h2 class="relative group flex items-center">
	<a rel="nofollow" href="#how-to-run-from-python-code" class="block pr-1.5 text-lg md:absolute md:p-1.5 md:opacity-0 md:group-hover:opacity-100 md:right-full" id="how-to-run-from-python-code">
		<span class="header-link"><svg viewBox="0 0 256 256" preserveAspectRatio="xMidYMid meet" height="1em" width="1em" role="img" aria-hidden="true" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-black dark:hover:text-gray-200 w-4"><path fill="currentColor" d="M167.594 88.393a8.001 8.001 0 0 1 0 11.314l-67.882 67.882a8 8 0 1 1-11.314-11.315l67.882-67.881a8.003 8.003 0 0 1 11.314 0zm-28.287 84.86l-28.284 28.284a40 40 0 0 1-56.567-56.567l28.284-28.284a8 8 0 0 0-11.315-11.315l-28.284 28.284a56 56 0 0 0 79.196 79.197l28.285-28.285a8 8 0 1 0-11.315-11.314zM212.852 43.14a56.002 56.002 0 0 0-79.196 0l-28.284 28.284a8 8 0 1 0 11.314 11.314l28.284-28.284a40 40 0 0 1 56.568 56.567l-28.285 28.285a8 8 0 0 0 11.315 11.314l28.284-28.284a56.065 56.065 0 0 0 0-79.196z"></path></svg></span>
	</a>
	<span>
		How to run from Python code
	</span>
</h2>
<p>You can use GGUF models from Python using the <a rel="nofollow" href="https://github.com/abetlen/llama-cpp-python">llama-cpp-python</a> or <a rel="nofollow" href="https://github.com/marella/ctransformers">ctransformers</a> libraries.</p>
<h3 class="relative group flex items-center">
	<a rel="nofollow" href="#how-to-load-this-model-in-python-code-using-ctransformers" class="block pr-1.5 text-lg md:absolute md:p-1.5 md:opacity-0 md:group-hover:opacity-100 md:right-full" id="how-to-load-this-model-in-python-code-using-ctransformers">
		<span class="header-link"><svg viewBox="0 0 256 256" preserveAspectRatio="xMidYMid meet" height="1em" width="1em" role="img" aria-hidden="true" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-black dark:hover:text-gray-200 w-4"><path fill="currentColor" d="M167.594 88.393a8.001 8.001 0 0 1 0 11.314l-67.882 67.882a8 8 0 1 1-11.314-11.315l67.882-67.881a8.003 8.003 0 0 1 11.314 0zm-28.287 84.86l-28.284 28.284a40 40 0 0 1-56.567-56.567l28.284-28.284a8 8 0 0 0-11.315-11.315l-28.284 28.284a56 56 0 0 0 79.196 79.197l28.285-28.285a8 8 0 1 0-11.315-11.314zM212.852 43.14a56.002 56.002 0 0 0-79.196 0l-28.284 28.284a8 8 0 1 0 11.314 11.314l28.284-28.284a40 40 0 0 1 56.568 56.567l-28.285 28.285a8 8 0 0 0 11.315 11.314l28.284-28.284a56.065 56.065 0 0 0 0-79.196z"></path></svg></span>
	</a>
	<span>
		How to load this model in Python code, using ctransformers
	</span>
</h3>
<p>Note: I have not tested ctransformers with Mistral models, but it may work if you set the <code>model_type</code> to <code>llama</code>.</p>
<h4 class="relative group flex items-center">
	<a rel="nofollow" href="#first-install-the-package" class="block pr-1.5 text-lg md:absolute md:p-1.5 md:opacity-0 md:group-hover:opacity-100 md:right-full" id="first-install-the-package">
		<span class="header-link"><svg viewBox="0 0 256 256" preserveAspectRatio="xMidYMid meet" height="1em" width="1em" role="img" aria-hidden="true" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-black dark:hover:text-gray-200 w-4"><path fill="currentColor" d="M167.594 88.393a8.001 8.001 0 0 1 0 11.314l-67.882 67.882a8 8 0 1 1-11.314-11.315l67.882-67.881a8.003 8.003 0 0 1 11.314 0zm-28.287 84.86l-28.284 28.284a40 40 0 0 1-56.567-56.567l28.284-28.284a8 8 0 0 0-11.315-11.315l-28.284 28.284a56 56 0 0 0 79.196 79.197l28.285-28.285a8 8 0 1 0-11.315-11.314zM212.852 43.14a56.002 56.002 0 0 0-79.196 0l-28.284 28.284a8 8 0 1 0 11.314 11.314l28.284-28.284a40 40 0 0 1 56.568 56.567l-28.285 28.285a8 8 0 0 0 11.315 11.314l28.284-28.284a56.065 56.065 0 0 0 0-79.196z"></path></svg></span>
	</a>
	<span>
		First install the package
	</span>
</h4>
<p>Run one of the following commands, according to your system:</p>
<pre><code class="language-shell"><span class="hljs-meta prompt_"># </span><span class="language-bash">Base ctransformers with no GPU acceleration</span>
pip install ctransformers
<span class="hljs-meta prompt_"># </span><span class="language-bash">Or with CUDA GPU acceleration</span>
pip install ctransformers[cuda]
<span class="hljs-meta prompt_"># </span><span class="language-bash">Or with AMD ROCm GPU acceleration (Linux only)</span>
CT_HIPBLAS=1 pip install ctransformers --no-binary ctransformers
<span class="hljs-meta prompt_"># </span><span class="language-bash">Or with Metal GPU acceleration <span class="hljs-keyword">for</span> macOS systems only</span>
CT_METAL=1 pip install ctransformers --no-binary ctransformers
</code></pre>
<h4 class="relative group flex items-center">
	<a rel="nofollow" href="#simple-ctransformers-example-code" class="block pr-1.5 text-lg md:absolute md:p-1.5 md:opacity-0 md:group-hover:opacity-100 md:right-full" id="simple-ctransformers-example-code">
		<span class="header-link"><svg viewBox="0 0 256 256" preserveAspectRatio="xMidYMid meet" height="1em" width="1em" role="img" aria-hidden="true" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-black dark:hover:text-gray-200 w-4"><path fill="currentColor" d="M167.594 88.393a8.001 8.001 0 0 1 0 11.314l-67.882 67.882a8 8 0 1 1-11.314-11.315l67.882-67.881a8.003 8.003 0 0 1 11.314 0zm-28.287 84.86l-28.284 28.284a40 40 0 0 1-56.567-56.567l28.284-28.284a8 8 0 0 0-11.315-11.315l-28.284 28.284a56 56 0 0 0 79.196 79.197l28.285-28.285a8 8 0 1 0-11.315-11.314zM212.852 43.14a56.002 56.002 0 0 0-79.196 0l-28.284 28.284a8 8 0 1 0 11.314 11.314l28.284-28.284a40 40 0 0 1 56.568 56.567l-28.285 28.285a8 8 0 0 0 11.315 11.314l28.284-28.284a56.065 56.065 0 0 0 0-79.196z"></path></svg></span>
	</a>
	<span>
		Simple ctransformers example code
	</span>
</h4>
<pre><code class="language-python"><span class="hljs-keyword">from</span> ctransformers <span class="hljs-keyword">import</span> AutoModelForCausalLM

<span class="hljs-comment"># Set gpu_layers to the number of layers to offload to GPU. Set to 0 if no GPU acceleration is available on your system.</span>
llm = AutoModelForCausalLM.from_pretrained(<span class="hljs-string">"TheBloke/Mistral-7B-v0.1-GGUF"</span>, model_file=<span class="hljs-string">"mistral-7b-v0.1.Q4_K_M.gguf"</span>, model_type=<span class="hljs-string">"mistral"</span>, gpu_layers=<span class="hljs-number">50</span>)

<span class="hljs-built_in">print</span>(llm(<span class="hljs-string">"AI is going to"</span>))
</code></pre>
<h2 class="relative group flex items-center">
	<a rel="nofollow" href="#how-to-use-with-langchain" class="block pr-1.5 text-lg md:absolute md:p-1.5 md:opacity-0 md:group-hover:opacity-100 md:right-full" id="how-to-use-with-langchain">
		<span class="header-link"><svg viewBox="0 0 256 256" preserveAspectRatio="xMidYMid meet" height="1em" width="1em" role="img" aria-hidden="true" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-black dark:hover:text-gray-200 w-4"><path fill="currentColor" d="M167.594 88.393a8.001 8.001 0 0 1 0 11.314l-67.882 67.882a8 8 0 1 1-11.314-11.315l67.882-67.881a8.003 8.003 0 0 1 11.314 0zm-28.287 84.86l-28.284 28.284a40 40 0 0 1-56.567-56.567l28.284-28.284a8 8 0 0 0-11.315-11.315l-28.284 28.284a56 56 0 0 0 79.196 79.197l28.285-28.285a8 8 0 1 0-11.315-11.314zM212.852 43.14a56.002 56.002 0 0 0-79.196 0l-28.284 28.284a8 8 0 1 0 11.314 11.314l28.284-28.284a40 40 0 0 1 56.568 56.567l-28.285 28.285a8 8 0 0 0 11.315 11.314l28.284-28.284a56.065 56.065 0 0 0 0-79.196z"></path></svg></span>
	</a>
	<span>
		How to use with LangChain
	</span>
</h2>
<p>Here are guides on using llama-cpp-python and ctransformers with LangChain:</p>
<ul>
<li><a rel="nofollow" href="https://python.langchain.com/docs/integrations/llms/llamacpp">LangChain + llama-cpp-python</a></li>
<li><a rel="nofollow" href="https://python.langchain.com/docs/integrations/providers/ctransformers">LangChain + ctransformers</a></li>
</ul>




<h2 class="relative group flex items-center">
	<a rel="nofollow" href="#discord" class="block pr-1.5 text-lg md:absolute md:p-1.5 md:opacity-0 md:group-hover:opacity-100 md:right-full" id="discord">
		<span class="header-link"><svg viewBox="0 0 256 256" preserveAspectRatio="xMidYMid meet" height="1em" width="1em" role="img" aria-hidden="true" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-black dark:hover:text-gray-200 w-4"><path fill="currentColor" d="M167.594 88.393a8.001 8.001 0 0 1 0 11.314l-67.882 67.882a8 8 0 1 1-11.314-11.315l67.882-67.881a8.003 8.003 0 0 1 11.314 0zm-28.287 84.86l-28.284 28.284a40 40 0 0 1-56.567-56.567l28.284-28.284a8 8 0 0 0-11.315-11.315l-28.284 28.284a56 56 0 0 0 79.196 79.197l28.285-28.285a8 8 0 1 0-11.315-11.314zM212.852 43.14a56.002 56.002 0 0 0-79.196 0l-28.284 28.284a8 8 0 1 0 11.314 11.314l28.284-28.284a40 40 0 0 1 56.568 56.567l-28.285 28.285a8 8 0 0 0 11.315 11.314l28.284-28.284a56.065 56.065 0 0 0 0-79.196z"></path></svg></span>
	</a>
	<span>
		Discord
	</span>
</h2>
<p>For further support, and discussions on these models and AI in general, join us at:</p>
<p><a rel="nofollow" href="https://discord.gg/theblokeai">TheBloke AI's Discord server</a></p>
<h2 class="relative group flex items-center">
	<a rel="nofollow" href="#thanks-and-how-to-contribute" class="block pr-1.5 text-lg md:absolute md:p-1.5 md:opacity-0 md:group-hover:opacity-100 md:right-full" id="thanks-and-how-to-contribute">
		<span class="header-link"><svg viewBox="0 0 256 256" preserveAspectRatio="xMidYMid meet" height="1em" width="1em" role="img" aria-hidden="true" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-black dark:hover:text-gray-200 w-4"><path fill="currentColor" d="M167.594 88.393a8.001 8.001 0 0 1 0 11.314l-67.882 67.882a8 8 0 1 1-11.314-11.315l67.882-67.881a8.003 8.003 0 0 1 11.314 0zm-28.287 84.86l-28.284 28.284a40 40 0 0 1-56.567-56.567l28.284-28.284a8 8 0 0 0-11.315-11.315l-28.284 28.284a56 56 0 0 0 79.196 79.197l28.285-28.285a8 8 0 1 0-11.315-11.314zM212.852 43.14a56.002 56.002 0 0 0-79.196 0l-28.284 28.284a8 8 0 1 0 11.314 11.314l28.284-28.284a40 40 0 0 1 56.568 56.567l-28.285 28.285a8 8 0 0 0 11.315 11.314l28.284-28.284a56.065 56.065 0 0 0 0-79.196z"></path></svg></span>
	</a>
	<span>
		Thanks, and how to contribute
	</span>
</h2>
<p>Thanks to the <a rel="nofollow" href="https://chirper.ai">chirper.ai</a> team!</p>
<p>Thanks to Clay from <a rel="nofollow" href="/TheBloke/Mistral-7B-v0.1-GGUF/blob/main/llm-utils">gpus.llm-utils.org</a>!</p>
<p>I've had a lot of people ask if they can contribute. I enjoy providing models and helping people, and would love to be able to spend even more time doing it, as well as expanding into new projects like fine tuning/training.</p>
<p>If you're able and willing to contribute it will be most gratefully received and will help me to keep providing more models, and to start work on new AI projects.</p>
<p>Donaters will get priority support on any and all AI/LLM/model questions and requests, access to a private Discord room, plus other benefits.</p>
<ul>
<li>Patreon: <a rel="nofollow" href="https://patreon.com/TheBlokeAI">https://patreon.com/TheBlokeAI</a></li>
<li>Ko-Fi: <a rel="nofollow" href="https://ko-fi.com/TheBlokeAI">https://ko-fi.com/TheBlokeAI</a></li>
</ul>
<p><strong>Special thanks to</strong>: Aemon Algiz.</p>
<p><strong>Patreon special mentions</strong>: Alicia Loh, Stephen Murray, K, Ajan Kanaga, RoA, Magnesian, Deo Leter, Olakabola, Eugene Pentland, zynix, Deep Realms, Raymond Fosdick, Elijah Stavena, Iucharbius, Erik Bjäreholt, Luis Javier Navarrete Lozano, Nicholas, theTransient, John Detwiler, alfie_i, knownsqashed, Mano Prime, Willem Michiel, Enrico Ros, LangChain4j, OG, Michael Dempsey, Pierre Kircher, Pedro Madruga, James Bentley, Thomas Belote, Luke @flexchar, Leonard Tan, Johann-Peter Hartmann, Illia Dulskyi, Fen Risland, Chadd, S_X, Jeff Scroggin, Ken Nordquist, Sean Connelly, Artur Olbinski, Swaroop Kallakuri, Jack West, Ai Maven, David Ziegler, Russ Johnson, transmissions 11, John Villwock, Alps Aficionado, Clay Pascal, Viktor Bowallius, Subspace Studios, Rainer Wilmers, Trenton Dambrowitz, vamX, Michael Levine, 준교 김, Brandon Frisco, Kalila, Trailburnt, Randy H, Talal Aujan, Nathan Dryer, Vadim, 阿明, ReadyPlayerEmma, Tiffany J. Kim, George Stoitzev, Spencer Kim, Jerry Meng, Gabriel Tamborski, Cory Kujawski, Jeffrey Morgan, Spiking Neurons AB, Edmond Seymore, Alexandros Triantafyllidis, Lone Striker, Cap'n Zoog, Nikolai Manek, danny, ya boyyy, Derek Yates, usrbinkat, Mandus, TL, Nathan LeClaire, subjectnull, Imad Khwaja, webtim, Raven Klaugh, Asp the Wyvern, Gabriel Puliatti, Caitlyn Gatomon, Joseph William Delisle, Jonathan Leane, Luke Pendergrass, SuperWojo, Sebastain Graf, Will Dee, Fred von Graf, Andrey, Dan Guido, Daniel P. Andersen, Nitin Borwankar, Elle, Vitor Caleffi, biorpg, jjj, NimbleBox.ai, Pieter, Matthew Berman, terasurfer, Michael Davis, Alex, Stanislav Ovsiannikov</p>
<p>Thank you to all my generous patrons and donaters!</p>
<p>And thank you again to a16z for their generous grant.</p>



<h1 class="relative group flex items-center">
	<a rel="nofollow" href="#original-model-card-mistral-ais-mistral-7b-v01" class="block pr-1.5 text-lg md:absolute md:p-1.5 md:opacity-0 md:group-hover:opacity-100 md:right-full" id="original-model-card-mistral-ais-mistral-7b-v01">
		<span class="header-link"><svg viewBox="0 0 256 256" preserveAspectRatio="xMidYMid meet" height="1em" width="1em" role="img" aria-hidden="true" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-black dark:hover:text-gray-200 w-4"><path fill="currentColor" d="M167.594 88.393a8.001 8.001 0 0 1 0 11.314l-67.882 67.882a8 8 0 1 1-11.314-11.315l67.882-67.881a8.003 8.003 0 0 1 11.314 0zm-28.287 84.86l-28.284 28.284a40 40 0 0 1-56.567-56.567l28.284-28.284a8 8 0 0 0-11.315-11.315l-28.284 28.284a56 56 0 0 0 79.196 79.197l28.285-28.285a8 8 0 1 0-11.315-11.314zM212.852 43.14a56.002 56.002 0 0 0-79.196 0l-28.284 28.284a8 8 0 1 0 11.314 11.314l28.284-28.284a40 40 0 0 1 56.568 56.567l-28.285 28.285a8 8 0 0 0 11.315 11.314l28.284-28.284a56.065 56.065 0 0 0 0-79.196z"></path></svg></span>
	</a>
	<span>
		Original model card: Mistral AI's Mistral 7B v0.1
	</span>
</h1>
<h1 class="relative group flex items-center">
	<a rel="nofollow" href="#model-card-for-mistral-7b-v01" class="block pr-1.5 text-lg md:absolute md:p-1.5 md:opacity-0 md:group-hover:opacity-100 md:right-full" id="model-card-for-mistral-7b-v01">
		<span class="header-link"><svg viewBox="0 0 256 256" preserveAspectRatio="xMidYMid meet" height="1em" width="1em" role="img" aria-hidden="true" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-black dark:hover:text-gray-200 w-4"><path fill="currentColor" d="M167.594 88.393a8.001 8.001 0 0 1 0 11.314l-67.882 67.882a8 8 0 1 1-11.314-11.315l67.882-67.881a8.003 8.003 0 0 1 11.314 0zm-28.287 84.86l-28.284 28.284a40 40 0 0 1-56.567-56.567l28.284-28.284a8 8 0 0 0-11.315-11.315l-28.284 28.284a56 56 0 0 0 79.196 79.197l28.285-28.285a8 8 0 1 0-11.315-11.314zM212.852 43.14a56.002 56.002 0 0 0-79.196 0l-28.284 28.284a8 8 0 1 0 11.314 11.314l28.284-28.284a40 40 0 0 1 56.568 56.567l-28.285 28.285a8 8 0 0 0 11.315 11.314l28.284-28.284a56.065 56.065 0 0 0 0-79.196z"></path></svg></span>
	</a>
	<span>
		Model Card for Mistral-7B-v0.1
	</span>
</h1>
<p>The Mistral-7B-v0.1 Large Language Model (LLM) is a pretrained generative text model with 7 billion parameters.
Mistral-7B-v0.1 outperforms Llama 2 13B on all benchmarks we tested.</p>
<p>For full details of this model please read our <a rel="nofollow" href="https://mistral.ai/news/announcing-mistral-7b/">Release blog post</a></p>
<h2 class="relative group flex items-center">
	<a rel="nofollow" href="#model-architecture" class="block pr-1.5 text-lg md:absolute md:p-1.5 md:opacity-0 md:group-hover:opacity-100 md:right-full" id="model-architecture">
		<span class="header-link"><svg viewBox="0 0 256 256" preserveAspectRatio="xMidYMid meet" height="1em" width="1em" role="img" aria-hidden="true" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-black dark:hover:text-gray-200 w-4"><path fill="currentColor" d="M167.594 88.393a8.001 8.001 0 0 1 0 11.314l-67.882 67.882a8 8 0 1 1-11.314-11.315l67.882-67.881a8.003 8.003 0 0 1 11.314 0zm-28.287 84.86l-28.284 28.284a40 40 0 0 1-56.567-56.567l28.284-28.284a8 8 0 0 0-11.315-11.315l-28.284 28.284a56 56 0 0 0 79.196 79.197l28.285-28.285a8 8 0 1 0-11.315-11.314zM212.852 43.14a56.002 56.002 0 0 0-79.196 0l-28.284 28.284a8 8 0 1 0 11.314 11.314l28.284-28.284a40 40 0 0 1 56.568 56.567l-28.285 28.285a8 8 0 0 0 11.315 11.314l28.284-28.284a56.065 56.065 0 0 0 0-79.196z"></path></svg></span>
	</a>
	<span>
		Model Architecture
	</span>
</h2>
<p>Mistral-7B-v0.1 is a transformer model, with the following architecture choices:</p>
<ul>
<li>Grouped-Query Attention</li>
<li>Sliding-Window Attention</li>
<li>Byte-fallback BPE tokenizer</li>
</ul>
<h2 class="relative group flex items-center">
	<a rel="nofollow" href="#the-mistral-ai-team" class="block pr-1.5 text-lg md:absolute md:p-1.5 md:opacity-0 md:group-hover:opacity-100 md:right-full" id="the-mistral-ai-team">
		<span class="header-link"><svg viewBox="0 0 256 256" preserveAspectRatio="xMidYMid meet" height="1em" width="1em" role="img" aria-hidden="true" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-black dark:hover:text-gray-200 w-4"><path fill="currentColor" d="M167.594 88.393a8.001 8.001 0 0 1 0 11.314l-67.882 67.882a8 8 0 1 1-11.314-11.315l67.882-67.881a8.003 8.003 0 0 1 11.314 0zm-28.287 84.86l-28.284 28.284a40 40 0 0 1-56.567-56.567l28.284-28.284a8 8 0 0 0-11.315-11.315l-28.284 28.284a56 56 0 0 0 79.196 79.197l28.285-28.285a8 8 0 1 0-11.315-11.314zM212.852 43.14a56.002 56.002 0 0 0-79.196 0l-28.284 28.284a8 8 0 1 0 11.314 11.314l28.284-28.284a40 40 0 0 1 56.568 56.567l-28.285 28.285a8 8 0 0 0 11.315 11.314l28.284-28.284a56.065 56.065 0 0 0 0-79.196z"></path></svg></span>
	</a>
	<span>
		The Mistral AI Team
	</span>
</h2>
<p>Albert Jiang, Alexandre Sablayrolles, Arthur Mensch, Chris Bamford, Devendra Singh Chaplot, Diego de las Casas, Florian Bressand, Gianna Lengyel, Guillaume Lample, Lélio Renard Lavaud, Lucile Saulnier, Marie-Anne Lachaux, Pierre Stock, Teven Le Scao, Thibaut Lavril, Thomas Wang, Timothée Lacroix, William El Sayed.</p>

<!-- HTML_TAG_END --></div>
</div></section></div></main>

	</div>

		<script>
			import("/front/build/kube-537c6d6/index.js");
			window.moonSha = "kube-537c6d6/";
		</script>

		<!-- Stripe -->
		<script>
			if (["hf.co", "huggingface.co"].includes(window.location.hostname)) {
				const script = document.createElement("script");
				script.src = "https://js.stripe.com/v3/";
				script.async = true;
				document.head.appendChild(script);
			}
		</script>
	</body>
</html>
