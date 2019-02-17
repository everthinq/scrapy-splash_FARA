# -*- coding: utf-8 -*-

lua_uncheck_country_represented_checkbox = """

--wait_for_element function is from documentation
function wait_for_element(splash, css, maxwait)
  -- Wait until a selector matches an element
  -- in the page. Return an error if waited more
  -- than maxwait seconds.
  if maxwait == nil then
      maxwait = 10
  end
  return splash:wait_for_resume(string.format([[
    function main(splash) {
      var selector = '%s';
      var maxwait = %s;
      var end = Date.now() + maxwait*1000;

      function check() {
        if(document.querySelector(selector)) {
          splash.resume('Element found');
        } else if(Date.now() >= end) {
          var err = 'Timeout waiting for element';
          splash.error(err + " " + selector);
        } else {
          setTimeout(check, 200);
        }
      }
      check();
    }
  ]], css, maxwait))
end

function main(splash, args)  
    assert(splash:go(args.url))
    wait_for_element(splash, "#apexir_CONTROL_PANEL_SUMMARY")
    
    --uncheck_CountryLocation_Represented_checkmark
    --unchecking this checkmark represents country in the data row (it makes easier to scrape)
    splash:evaljs("document.querySelectorAll('input[type=checkbox]')[0].click();")
    wait_for_element(splash, "#apexir_COUNTRY_NAME")
    
    return {
        cookies = splash:get_cookies(),
        html = splash:html()
    }
end

"""

lua_page_next = """

--wait_for_element function is from documentation
function wait_for_element(splash, css, maxwait)
  -- Wait until a selector matches an element
  -- in the page. Return an error if waited more
  -- than maxwait seconds.
  if maxwait == nil then
      maxwait = 10
  end
  return splash:wait_for_resume(string.format([[
    function main(splash) {
      var selector = '%s';
      var maxwait = %s;
      var end = Date.now() + maxwait*1000;

      function check() {
        if(document.querySelector(selector)) {
          splash.resume('Element found');
        } else if(Date.now() >= end) {
          var err = 'Timeout waiting for element';
          splash.error(err + " " + selector);
        } else {
          setTimeout(check, 200);
        }
      }
      check();
    }
  ]], css, maxwait))
end

function main(splash, args)  
    assert(splash:go(args.url))
    splash:init_cookies(splash.args.cookies)

    wait_for_element(splash, "#apexir_CONTROL_PANEL_SUMMARY")
    splash:evaljs('document.querySelector("[title=\'Next\']").click();')
    wait_for_element(splash, '#apexir_WORKSHEET_DATA') 
    
    return {
        html = splash:html()
    }
end

"""