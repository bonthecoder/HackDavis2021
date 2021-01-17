chrome.runtime.onInstalled.addListener(function() {
  chrome.storage.sync.set({color: '#3aa757'}, function() {
    console.log('The color is green.');
  });

  // replace all rules
  chrome.declarativeContent.onPageChanged.removeRules(undefined, function() {
    // with a new rule
    chrome.declarativeContent.onPageChanged.addRules([{
      // fires when a page URL host is canvas.ucdavis.edu
      conditions: [new chrome.declarativeContent.PageStateMatcher({
        pageUrl: {hostEquals: 'canvas.ucdavis.edu'},
      })
      ],
        // shows the extension page's action
        actions: [new chrome.declarativeContent.ShowPageAction()]
    }]);
  });
});