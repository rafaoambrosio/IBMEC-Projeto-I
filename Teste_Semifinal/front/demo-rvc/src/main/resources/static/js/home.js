
				document.addEventListener("scroll", function () {
					const header = document.querySelector(".default-header");
					const banner = document.querySelector(".banner-area");
					const bannerBottom = banner.offsetHeight;

					if (window.scrollY > 1) { 
						header.classList.add("scrolled");
					} else {
						header.classList.remove("scrolled");
					}

					if (window.scrollY > bannerBottom) { 
						header.classList.add("navbar-bottom-border");
					} else {
						header.classList.remove("navbar-bottom-border");
					}
				});

				