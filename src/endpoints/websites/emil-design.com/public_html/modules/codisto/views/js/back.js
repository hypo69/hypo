/**
* 2022 Codisto
*
* NOTICE OF LICENSE
*
* This source file is subject to the 3-Clause BSD License
* that is bundled with this package in the file LICENSE.txt.
* It is also available through the world-wide-web at this URL:
* https://opensource.org/licenses/BSD-3-Clause
* If you did not receive a copy of the license and are unable to
* obtain it through the world-wide-web, please send an email
* to support@codisto.com so we can send you a copy immediately.
*
* DISCLAIMER
*
* Do not edit or add to this file if you wish to upgrade Codisto to newer
* versions in the future. If you wish to customize Codisto for your
* needs please refer to https://codisto.com for more information.
*
*  @author    Codisto <support@codisto.com>
*  @copyright 2022 Codisto
*  @license   https://opensource.org/licenses/BSD-3-Clause 3-Clause BSD License
*  Property of Codisto
*
* Don't forget to prefix your containers with your own identifier
* to avoid any conflicts with others containers.
*/

(function() {

	document.addEventListener("DOMContentLoaded", function() {

		const templateBody = document.querySelectorAll("BODY");
		if(templateBody.length) {

			document.querySelectorAll(".new-template").forEach(function(el) {

				el.addEventListener("click", function(e) {

					document.location = window.location.href + "&file=_new";

				});

			});

			document.querySelectorAll("#filename").forEach(function(el) {

				el.focus();

			});

		}

		const templateForm = document.querySelector("form#template");
		if(templateForm) {
			templateForm.addEventListener("submit", function(e){

				const filename = document.querySelector("#template input[name=file]").value;
				const re = /[^a-zA-Z0-9\_\-\.]/g;
				const ext = /(\.html)$/i;
				if(filename == '') {
					e.preventDefault();
					document.getElementById("error-message").innerHTML = '<p style="color:red"><strong>The file name is required.</strong></p>';
				}
				else if(re.test(filename)) {
					e.preventDefault();
					document.getElementById("error-message").innerHTML = '<p style="color:red"><strong>The file name provided is invalid. Please only use ‘-’, ‘_’, ‘.’ and alphanumeric characters.</strong></p>';
				}else if (!ext.exec(filename)) {
					e.preventDefault();
					document.getElementById("error-message").innerHTML = '<p style="color:red"><strong>The file name provided is invalid. Only .html extensions are allowed.</strong></p>';
				} else {
					document.getElementById("error-message").innerHTML = '';
				}
			});
		}

	});

})();

(function() {

	const checkButton = function() {

		const email = document.querySelector("#codisto-form input[name=email]").value;
		const emailconfirm = document.querySelector("#codisto-form input[name=emailconfirm]").value;
		const phone = document.querySelector("#codisto-form input[name=phone]").value;
		let invalid = true;
		if (email && !/^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/.test(email))
		{
			document.querySelector(".email-help-text").innerHTML = document.querySelector(".email-help-text").dataset.invalidmessage;
		} else if(!email) {
			document.querySelector(".email-help-text").innerHTML = document.querySelector(".email-help-text").dataset.defaultmessage;
		} else {
			invalid = invalid && false;
			document.querySelector(".email-help-text").innerHTML = "";
		}
		if (emailconfirm && !/^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/.test(emailconfirm))
		{
			document.querySelector(".emailconfirm-help-text").innerHTML = document.querySelector(".emailconfirm-help-text").dataset.invalidmessage;
		} else if(!emailconfirm) {
			document.querySelector(".emailconfirm-help-text").innerHTML = document.querySelector(".emailconfirm-help-text").dataset.defaultmessage;
		} else {
			invalid = invalid && false;
			document.querySelector(".emailconfirm-help-text").innerHTML = "";
		}
		if (phone && !/(\+?)\d{10,14}$/.test(phone))
		{
			document.querySelector(".phone-help-text").innerHTML = document.querySelector(".phone-help-text").dataset.invalidmessage;
		} else if(!phone) {
			document.querySelector(".phone-help-text").innerHTML = document.querySelector(".phone-help-text").dataset.defaultmessage;
		} else {
			invalid = invalid && false;
			document.querySelector(".phone-help-text").innerHTML = "";
		}
		if (!invalid && email && emailconfirm
			&& (email == emailconfirm)) {
			document.querySelector(".error-message").style.display = "none";
			document.querySelector("#codisto-form .next BUTTON").classList.add("button-primary");
		} else {
			document.querySelector("#codisto-form .next BUTTON").classList.remove("button-primary");
		}

	};

	document.addEventListener("DOMContentLoaded", function() {

		var codistoForm = document.querySelector("form#codisto-form");

		if(codistoForm) {

			document.querySelector("#create-account-modal .selection").style.opacity = 0.1;

			function jsonp(url, callback) {
				var callbackName = 'jsonp_callback_' + Math.round(100000 * Math.random());
				var script = document.createElement('script');

				script.src = url + (url.indexOf('?') >= 0 ? '&' : '?') + 'callback=' + callbackName;
				document.body.appendChild(script);

				window[callbackName] = function(data) {
					delete window[callbackName];
					document.body.removeChild(script);
					callback(data);
				};
			}

			jsonp("http://ui.codisto.com/getcountrylist", function(data) {
				document.querySelector(".select-html-wrapper").innerHTML = data;
				document.querySelector("#create-account-modal .selection").style.opacity = 1;
			});

			codistoForm.addEventListener("change", checkButton);
			codistoForm.addEventListener("keyup", checkButton);
			codistoForm.addEventListener("submit", function(e) {

				const email = codistoForm.querySelector("INPUT[name=email]").value;
				const emailConfirm = codistoForm.querySelector("INPUT[name=emailconfirm]").value;
				if (email != emailConfirm) {
					e.stopPropagation();
					e.preventDefault();
					document.querySelector(".error-message").style.display = "block";
				} else {
					document.querySelector(".error-message").style.display = "none";
				}

			});

		}

	});

})();
