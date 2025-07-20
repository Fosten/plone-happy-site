const applyConfig = (config) => {
  config.settings = {
    ...config.settings,
    matomoSiteId: '1',
    matomoUrlBase: 'https://stats.happybaseball.com/',
    showPloneLogin: false,
    serverConfig: {
      ...config.settings.serverConfig,
      extractScripts: {
        ...config.settings.serverConfig.extractScripts,
        errorPages: true,
      },
    },
  };
  return config;
};

export default applyConfig;
