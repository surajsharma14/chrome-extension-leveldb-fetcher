chrome.runtime.onInstalled.addListener(() => {
  chrome.storage.local.set({ hello: "world" }, () => {
    console.log("Value is set to 'hello: world'");
  });
});
