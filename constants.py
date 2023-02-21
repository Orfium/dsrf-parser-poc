SOUND_RECORDING_HEADERS = [
    "AssetID",
    "Title",
    "Artist",
    "Writers",
    "ISRC",
    "Views",
    "Tag"
]


COMPOSITION_HEADERS = [
    "AssetID",
    "Title",
    "Artist",
    "Writers",
    "ISWC",
    "Views",
    "Tag"
]


# Digital Sales Reporting Message Suite Standard - Record Type Definitions (Version 1.4)
RECORDS = {
    # Header and Footer Record Types
    "HEAD": ["RecordType", "MessageVersion", "Profile", "ProfileVersion", "MessageId", "MessageCreatedDateTime",
             "FileNumber", "NumberOfFiles", "UsageStartDate", "UsageEndDate", "SenderPartyId", "SenderName",
             "ServiceDescription", "RecipientPartyId", "RecipientName", "RepresentedRepertoire"],  # Header Record
    "FOOT": ["RecordType", "NumberOfLinesInFile", "NumberOfLinesInReport", "NumberOfSummaryRecords",
             "NumberOfBlocksInFile", "NumberOfBlocksInReport"],  # Footer Record
    "SRFO": ["RecordType", "NumberOfLinesInReport", "NumberOfSummaryRecords"],
    # Footer Record For Single-Record Block Variants

    # Summary Record Types
    "SY01.02": ["RecordType", "SummaryRecordId", "DistributionChannel", "DistributionChannelDPID", "CommercialModel",
                "UseType", "Territory", "ServiceDescription", "TotalUsages", "Subscribers", "CurrencyOfReporting",
                "NetRevenue", "IndirectValue", "CurrencyOfTransaction", "ExchangeRate"],  # Basic Summary Record
    "SY02.03": ["RecordType", "SummaryRecordId", "DistributionChannel", "DistributionChannelDPID", "CommercialModel",
                "UseType", "Territory", "ServiceDescription", "TotalUsages", "Users", "CurrencyOfReporting",
                "NetRevenue", "RightsController", "RightsControllerPartyId", "AllocatedUsages", "AllocatedRevenue",
                "AllocatedNetRevenue", "RightsType", "ContentCategory", "CurrencyOfTransaction", "ExchangeRate",
                "RightsTypePercentage"],  # Summary Record for Ad-Supported and Interactive Streaming Services
    "SY03.01": ["RecordType", "SummaryRecordId", "DistributionChannel", "DistributionChannelDPID", "CommercialModel",
                "UseType", "Territory", "ServiceDescription", "TotalUsages", "Subscribers", "CurrencyOfReporting",
                "NetRevenue", "RightsController", "RightsControllerPartyId", "AllocatedUsages", "AllocatedRevenue",
                "AllocatedNetRevenue", "RightsControllerMarketShare", "ConsumerPaidUnitPrice", "FreeOrTrialSubscribers",
                "CurrencyOfTransaction", "ExchangeRate", "SubscriberType"],  # Summary Record for Subscription Services
    "SY04.01": ["RecordType", "SummaryRecordId", "DistributionChannel", "DistributionChannelDPID", "CommercialModel",
                "UseType", "Territory", "ServiceDescription", "SubscriberType", "Subscribers", "SubPeriodStartDate",
                "SubPeriodEndDate", "TotalUsagesInSubPeriod", "TotalUsagesInReportingPeriod", "CurrencyOfReporting",
                "CurrencyOfTransaction", "ExchangeRate", "ConsumerPaidUnitPrice", "NetRevenue", "MusicUsagePercentage"],
    # Per-subscriber Minima Summary Record for Subscription Services
    "SY05.03": ["RecordType", "SummaryRecordId", "DistributionChannel", "DistributionChannelDPID", "CommercialModel",
                "UseType", "Territory", "ServiceDescription", "RightsController", "RightsControllerPartyId",
                "RightsType", "TotalUsages", "AllocatedUsages", "MusicUsagePercentage", "AllocatedNetRevenue",
                "AllocatedRevenue", "RightsControllerMarketShare", "CurrencyOfReporting", "CurrencyOfTransaction",
                "ExchangeRate", "Deprecated Cell", "SubPeriodStartDate", "SubPeriodEndDate", "ContentCategory",
                "RightsTypePercentage", "ParentSummaryRecordId"],
    # Licensor Usage and Revenue Summary Record for Subscription Services
    "SY06.01": ["RecordType", "SummaryRecordId", "DistributionChannel", "DistributionChannelDPID", "CommercialModel",
                "UseType", "Territory", "ServiceDescription", "TotalUsages", "Subscribers", "CurrencyOfReporting",
                "NumberOfReleases", "NetRevenue", "IndirectValue", "PreviewAvailable", "CurrencyOfTransaction",
                "ExchangeRate", "ViewerHours"],  # Summary Record for AV Content
    "SY07.01": ["RecordType", "SummaryRecordId", "DistributionChannel", "DistributionChannelDPID", "CommercialModel",
                "UseType", "Territory", "RightsType", "ServiceDescription", "TotalUsages", "Users",
                "CurrencyOfReporting", "NetRevenue", "RightsController", "RightsControllerPartyId", "AllocatedUsages",
                "AllocatedRevenue", "AllocatedNetRevenue", "CurrencyOfTransaction", "ExchangeRate",
                "RightsTypePercentage"],  # Summary Record for Royalty Reports
    "SY08.02": ["RecordType", "SummaryRecordId", "DistributionChannel", "DistributionChannelDPID", "ServiceDescription",
                "BroadcastOrChannel", "CommercialModel", "UseType", "Territory", "NumberOfBroadcasts",
                "NumberOfBroadcastListeners", "ListenerHours", "CurrencyOfReporting", "NetRevenue", "IndirectValue",
                "RightsController", "RightsControllerPartyID", "AllocatedRevenue", "RightsType", "AllocatedNetRevenue",
                "RightsControllerAllocatedNumberOfBroadcasts", "AdditionalData", "CurrencyOfTransaction",
                "ExchangeRate", "RightsTypePercentage"],  # Summary Record for Broadcast Reports
    "SY09.01": ["RecordType", "SummaryRecordId", "CommercialModel", "UseType", "Territory", "ServiceDescription",
                "Deprecated Cell", "RightsController", "RightsControllerPartyID", "RightsType", "TotalUsages",
                "AllocatedUsages", "NetRevenue", "IndirectValue", "RightsControllerMarketShare", "CurrencyOfReporting",
                "CurrencyOfTransaction", "ExchangeRate", "RightsTypePercentage", "SubPeriodStartDate",
                "SubPeriodEndDate", "ParentSummaryRecordId"],
    # Summary Record to communicate Rights Controller Market Shares
    "SY10.01": ["RecordType", "SummaryRecordId", "DistributionChannel", "DistributionChannelDPID", "CommercialModel",
                "UseType", "ReportingPeriodStartDate", "ReportingPeriodEndDate", "SubscriberType", "Subscribers",
                "ActiveSubscribers", "PromotionalActivity", "Territory", "ServiceDescription", "OfferType", "Quality",
                "TotalUsages", "AllocatedUsages", "Returns", "MusicUsagePercentage", "CurrencyOfTransaction",
                "CurrencyOfAccounting", "ExchangeRate", "ExchangeRateSource", "DateOfCurrencyExchange",
                "GrossRevenueInCurrencyOfTransaction", "GrossRevenueInCurrencyOfAccounting", "CalculationType",
                "CalculationValue", "DeductionType", "DeductionsInCurrencyOfTransaction",
                "DeductionsInCurrencyOfAccounting", "NetRevenueInCurrencyOfTransaction",
                "NetRevenueInCurrencyOfAccounting", "AllocatedRevenueInCurrencyOfTransaction",
                "AllocatedRevenueInCurrencyOfAccounting", "AllocatedNetRevenueInCurrencyOfTransaction",
                "AllocatedNetRevenueInCurrencyOfAccounting", "RightsControllerMarketShare",
                "SubscriptionFeeInCurrencyOfTransaction", "SubscriptionFeeInCurrencyOfAccounting",
                "UsageIndependentFeeType", "UsageIndependentFeeInCurrencyOfTransaction",
                "UsageIndependentFeeInCurrencyOfAccounting", "FinalTotalAmountInCurrencyOfTransaction",
                "FinalTotalAmountInCurrencyOfAccounting"],
    # Summary Record Type for Financial Reporting to Record Companies
    "SY11.01": ["RecordType", "SummaryRecordId", "DistributionChannel", "DistributionChannelDPID", "CommercialModel",
                "UseType", "Territory", "ServiceDescription", "UsageForPrioritisaiton"],
    # Basic Summary Record for Masterlist Communications
    "SY12": ["RecordType", "SummaryRecordId", "DistributionChannel", "DistributionChannelDPID", "CommercialModel",
             "UseType", "Territory", "ServiceDescription", "TotalUsages", "Subscribers", "CurrencyOfReporting",
             "NetRevenue", "IndirectValue", "CurrencyOfTransaction", "ExchangeRate",
             "TotalCostOfContentInCurrencyOfReporting", "PerformanceRoyaltiesIn CurrencyOfReporting"],
    # Basic Summary Record for communication with the US Mechanical Licensing Collective

    # Release Record Types
    "RE01.02": ["RecordType", "BlockId", "ReleaseReference", "DspReleaseId", "ProprietaryReleaseId",
                "ReleaseCatalogNumber", "ReleaseICPN", "ReleaseDisplayArtistName", "ReleaseDisplayArtistPartyId",
                "ReleaseTitle", "ReleaseSubTitle", "ReleaseType", "ReleaseLabelName", "ReleasePLine",
                "DataProviderName", "ReleaseDate"],  # Basic Audio Release Record
    "RE02": ["RecordType", "BlockId", "ReleaseReference", "DspSubReleaseId", "ProprietarySubReleaseId",
             "UsedResources"],  # Basic Sub-Release Record
    "RE03.02": ["RecordType", "BlockId", "ReleaseReference", "DspReleaseId", "ProprietaryReleaseId", "ReleaseICPN",
                "ReleaseTitle", "ReleaseSubTitle", "SeriesTitle", "SeasonNumber", "ReleaseDisplayArtistName",
                "ReleaseDisplayArtistPartyId", "ReleaseType", "DataProviderName", "VideoCategory", "EpisodeNumber",
                "UserChannelName"],  # Audio-visual Release Record
    "RE04": ["RecordType", "BlockId", "ReleaseReference", "DspReleaseId", "ProprietaryReleaseId",
             "ReleaseCatalogNumber", "ReleaseICPN", "ReleaseDisplayArtistName", "ReleaseDisplayArtistPartyId",
             "ReleaseTitle", "ReleaseSubTitle", "ReleaseType", "ReleaseLabelName", "ReleasePLine", "DataProviderName",
             "ReleaseDate", "ReleaseDisplayArtistNameAsReceived", "ReleaseDisplayArtistAsReceived",
             "ReleaseTitleAsReceived", "ReleaseSubTitleAsReceived", "AlternativeReleaseTitle",
             "AlternativeReleaseTitleAsReceived"],
    # Audio Release Record for communicating with The Mechanical Licensing Collective

    # Resource Record Types
    "AS01.02": ["RecordType", "BlockId", "ResourceReference", "DspResourceId", "ResourceISRC", "ResourceTitle",
                "ResourceSubTitle", "ResourceDisplayArtistName", "ResourceDisplayArtistPartyId", "ResourceDuration",
                "ResourceType", "IsMasterRecording", "IsSubjectTo", "OwnershipConflict", "LastConflictCheck"],
    # Basic Sound Recording Record
    "AS02.03": ["RecordType", "BlockId", "ResourceReference", "DspResourceId", "ResourceISRC", "ResourceTitle",
                "ResourceSubTitle", "ResourceDisplayArtistName", "ResourceDisplayArtistPartyId", "ResourceDuration",
                "ResourceType", "MusicalWorkISWC", "MusicalWorkComposerAuthorName", "MusicalWorkComposerAuthorPartyId",
                "MusicalWorkArrangerName", "MusicalWorkArrangerPartyId", "MusicPublisherName", "MusicPublisherPartyId",
                "MusicalWorkContributorName", "MusicalWorkContributorPartyId", "ProprietaryMusicalWorkId",
                "IsMasterRecording", "IsSubjectToOwnershipConflict", "LastConflictCheck"],
    # Basic Sound Recording Record with Musical Work Details
    "AS03.02": ["RecordType", "BlockId", "ResourceReference", "DspResourceId", "ISAN", "EIDR", "ProprietaryResourceId",
                "VideoType", "ResourceTitle", "ResourceSubTitle", "OriginalResourceTitle", "SeasonNumber",
                "EpisodeNumber", "ResourceGenre", "ResourceDuration", "ResourceProducerName", "ResourceProducerPartyId",
                "ResourceDirectorName", "ResourceDirectorPartyId", "ResourceActorName", "ResourceActorPartyId",
                "LanguageLocalizationType", "HasCaptioning", "HasAudioDescription", "OriginalLanguageOfPerformance",
                "LanguageOfDubbing", "DateOfProductionOrRelease", "CountryOfResourceProduction",
                "OriginalBroadcastDateTime", "ResourceProductionCompanyName", "ResourceProductionCompanyPartyId",
                "CueSheetDataProviderName"],  # Audio-visual Resource Record
    "AS04": ["RecordType", "BlockId", "ResourceReference", "ResourceType"],  # Resource Record for Websites
    "AS05": ["RecordType", "BlockId", "ResourceReference", "DspResourceId", "ISRC", "ResourceTitle", "ResourceSubTitle",
             "ResourceDisplayArtistName", "ResourceDisplayArtistPartyId", "ResourceDuration", "ResourceType",
             "IsMasterRecording", "IsSubjectToOwnershipConflict", "LastConflictCheck", "ResourceStudioProducerName",
             "ResourceStudioProducerPartyId", "AlternativeResourceTitle", "ResourceDisplayArtistNameAsReceived",
             "ResourceDisplayArtistAsReceived", "ResourceTitleAsReceived", "ResourceSubTitleAsReceived",
             "AlternativeResourceTitleAsReceived", "ResourceIngestionDate", "EstimatedResourceIngestionDate",
             "ResourceAvailabilityDate", "EstimatedResourceAvailabilityDate"],
    # Basic Sound Recording Record for communicating with The Mechanical Licensing Collective
    "AS06": ["RecordType", "BlockId", "ResourceReference", "DspResourceId", "ResourceISRC", "ResourceTitle",
             "ResourceSubTitle", "ResourceDisplayArtistName", "ResourceDisplayArtistPartyId", "ResourceDuration",
             "ResourceType", "MusicalWorkISWC", "MusicalWorkComposerAuthorName", "MusicalWorkComposerAuthorPartyId",
             "MusicalWorkArrangerName", "MusicalWorkArrangerPartyId", "MusicPublisherName", "MusicPublisherPartyId",
             "MusicalWorkContributorName", "MusicalWorkContributorPartyId", "ProprietaryMusicalWorkId",
             "IsMasterRecording", "IsSubjectToOwnershipConflict", "LastConflictCheck", "ResourceStudioProducerName",
             "ResourceStudioProducerPartyId", "AlternativeResourceTitle", "MusicalWorkTitle", "MusicalWorkSubTitle",
             "ResourceTitleAsReceived", "ResourceSubTitleAsReceived", "AlternativeResourceTitleAsReceived",
             "ResourceDisplayArtistNameAsReceived", "ResourceDisplayArtistAsReceived", "AlternativeMusicalWorkTitle",
             "ResourceIngestionDate", "EstimatedResourceIngestionDate", "ResourceAvailabilityDate",
             "EstimatedResourceAvailabilityDate"],
    # Basic Sound Recording Record with Musical Work Details for communicating with The Mechanical Licensing Collective
    "LC01": ["RecordType", "BlockId", "ResourceReference", "DspResourceId", "ISRC", "ResourceTitle", "ResourceSubTitle",
             "ResourceDisplayArtistName", "ResourceDisplayArtistPartyId", "ResourceDuration", "ResourceType",
             "MusicalWorkISWC", "MusicalWorkComposerAuthorName", "MusicalWorkComposerAuthorPartyId",
             "MusicalWorkArrangerName", "MusicalWorkArrangerPartyId", "MusicPublisherName", "MusicPublisherPartyId",
             "MusicalWorkContributorName", "MusicalWorkContributorPartyId", "ProprietaryMusicalWorkId",
             "DataProviderName", "IsSubjectToOwnershipConflict"],
    # Resource and Work Record as provided by a Record Company

    # Work and Cue Record Types
    "MW01.02": ["RecordType", "BlockId", "DspMusicalWorkId", "MusicalWorkISWC", "MusicalWorkTitle",
                "MusicalWorkSubTitle", "MusicalWorkComposerAuthorName", "MusicalWorkComposerAuthorPartyId",
                "MusicalWorkArrangerName", "MusicalWorkArrangerPartyId", "MusicPublisherName", "MusicPublisherPartyId",
                "MusicalWorkContributorName", "MusicalWorkContributorPartyId", "DataProviderName",
                "ProprietaryMusicalWorkId", "ResourceReference", "ParentLicensorDataRecordId", "ParentMasterlistId"],
    # Basic Musical Work Record
    "MW02": ["RecordType", "BlockId", "DspWorkId", "MusicalWorkISWC", "MusicalWorkTitle", "MusicalWorkSubTitle",
             "MusicalWorkComposerAuthorName", "MusicalWorkComposerAuthorPartyId", "MusicalWorkArrangerName",
             "MusicalWorkArrangerPartyId", "MusicPublisherName", "MusicPublisherPartyId", "MusicalWorkContributorName",
             "MusicalWorkContributorPartyId", "DataProviderName", "ProprietaryWorkId", "ResourceReference",
             "ParentLicensorDataRecordId", "ParentMasterlistId", "MusicalWorkReference", "AlternativeMusicalWorkTitle"],
    # Basic Musical Work Record for communicating with The Mechanical Licensing Collective.
    "CU01.01": ["RecordType", "BlockId", "ResourceReference", "CueStartTime", "CueDuration", "ReferencedCreationISRC",
                "ReferencedCreationISWC", "ReferencedCreationTitle", "ReferencedCreationDisplayArtistName",
                "ReferencedCreationDisplayArtistPartyId", "ReferencedCreationContributorName",
                "ReferencedCreationContributorPartyId", "ReferencedCreationComposerAuthorName",
                "ReferencedCreationComposerAuthorPartyId", "ReferencedCreationArrangerName",
                "ReferencedCreationArrangerPartyId", "CueSheetDataProviderName"],  # Basic Cue Record
    "CU02": ["RecordType", "BlockId", "ResourceReference", "DspWorkId", "ProprietaryWorkId", "WorkTitle", "WorkType",
             "CreationOrReleaseDate", "WorkContributorName", "WorkContributorPartyId", "WorkContributorRole",
             "BroadcastStartTime", "BroadcastDuration", "LengthOfText", "LanguageAndCharacterCoding",
             "WorkPublisherName", "WorkPublisherId", "WorkProducerName", "WorkProducerId"],
    # Cue Record for Graphical and Literary Works
    "RC01": ["RecordType", "BlockId", "ResourceReference", "MusicalWorkReference", "RightsControllerName",
             "RightsControllerPartyId", "RightsType", "RightShare", "IsAffiliatedWithLicensee"],
    # Rights Controller Record

    # Record Types to provide Sales and / or Usage Data
    "SU01.02": ["RecordType", "BlockId", "SummaryRecordId", "SalesTransactionId", "TransactedRelease",
                "TransactedResource", "IsRoyaltyBearing", "SalesUpgrade", "Usages", "Returns",
                "PriceConsumerPaidExcSalesTax", "PromotionalActivity", "UseType"],
    # Usage, Revenue or Sales Record for Download Services
    "SU02.02": ["RecordType", "BlockId", "SummaryRecordId", "SalesTransactionId", "TransactedRelease",
                "TransactedResource", "IsRoyaltyBearing", "NumberOfStreams", "PriceConsumerPaidExcSalesTax",
                "PromotionalActivity", "UseType"],  # Usage, Revenue or Sales Record for Streaming Services and Webcasts
    "SU03.02": ["RecordType", "BlockId", "SalesTransactionId", "SummaryRecordId", "DspResourceId", "Usages",
                "NetRevenue", "ValidityPeriodStart", "ValidityPeriodEnd", "ContentCategory", "IsRoyaltyBearing"],
    # UGC Sales and Usage Record
    "SU04.02": ["RecordType", "BlockId", "SummaryRecordId", "SalesTransactionId", "TransactedRelease",
                "TransactedResource", "IsDrmEnforced", "VideoDefinitionType", "CodingType", "BitRate",
                "OriginalBroadcastChannel", "OriginalBroadcastDateTime", "IsRoyaltyBearing", "SalesUpgrade", "Usages",
                "Returns", "DurationUsed", "PriceConsumerPaidExcSalesTax", "PromotionalActivity", "OfferStartDate",
                "OfferEndDate", "OfferURL", "OriginalBroadcastDateTime", "UseType"],  # AV-specific Usage Record
    "SU05.01": ["RecordType", "BlockId", "SummaryRecordId", "SalesTransactionId", "TransactedResource",
                "IsRoyaltyBearing", "NumberOfBroadcasts", "NumberOfBroadcastListeners", "ListenerDuration", "UseType"],
    # Usage, Revenue or Sales Record for Broadcasts
    "SU06": ["RecordType", "BlockId", "SummaryRecordId", "SalesTransactionId", "TransactedResource", "Usages",
             "OfferURL"],  # Usages for Graphical and Literary Works
    "RU01.02": ["RecordType", "BlockId", "SummaryRecordId", "DspReleaseId", "Usages", "ContentCategory",
                "ParentResourceReference"],  # UGC Release Usage Summary Record
    "RU02.02": ["RecordType", "BlockId", "SummaryRecordId", "DspReleaseId", "ReleaseTitle", "ReleaseURL", "Usages",
                "ContentCategory", "ParentResourceReference"],  # UGC Release Usage Record
    "LI01.03": ["RecordType", "BlockId", "SummaryRecordId", "RightsController", "RightsControllerPartyId",
                "RightsControllerWorkId", "RightShare", "RightsType", "AllocatedNetRevenue", "AllocatedAmount",
                "AllocatedUsages", "ParentSalesTransactionId", "LicensorDataRecordId"],
    # Licensor-specific Usage Data Record
    "ST01": ["RecordType", "BlockId", "ParentSalesTransactionId", "SummaryRecordId", "Usages"],
    # Subscriber Type Record for UGC Business Models

    # Miscellaneous Record Types
    "ML01.01": ["RecordType", "BlockId", "SummaryRecordId", "ResourceReference", "UsageForPrioritisation",
                "PercentileForPrioritisation", "UnclaimedPercentage", "MasterlistId"],
    # Multiple Record Block Record for the Masterlist Profile
    "DExx": [],  # Deal-specific Records

    # Record Types for Single Record Block Variants
    "SR01.01": ["RecordType", "SummaryRecordId", "DspResourceId", "ISRC", "ResourceTitle", "ResourceSubTitle",
                "ResourceDisplayArtistName", "ResourceDisplayArtistPartyId", "Duration", "ResourceType",
                "ProprietaryWorkId", "ISWC", "ComposerAuthorName", "ComposerAuthorPartyId", "ArrangerName",
                "ArrangerPartyId", "MusicPublisherName", "MusicPublisherPartyId", "WorkContributorName",
                "WorkContributorPartyId", "DspReleaseId", "ProprietaryReleaseId", "ReleaseCatalogNumber", "ICPN",
                "ReleaseDisplayArtistName", "ReleaseDisplayArtistPartyId", "ReleaseTitle", "ReleaseSubTitle",
                "ReleaseType", "ReleaseLabelName", "PLine", "ReleaseDataProviderName", "NumberOfTransactedResources",
                "SalesTransactionId", "IsRoyaltyBearing", "SalesUpgrade", "Downloads", "Returns",
                "PriceConsumerPaidExcSalesTax", "CalculatedPriceConsumerPaidForResourceExcSalesTax",
                "PromotionalActivity", "ReleaseDate", "UseType"],
    # SRB Record Type for the Basic Audio Profile for Download Models
    "SR02.01": ["RecordType", "SummaryRecordId", "DspResourceId", "ISRC", "ResourceTitle", "ResourceSubTitle",
                "ResourceDisplayArtistName", "ResourceDisplayArtistPartyId", "Duration", "ResourceType",
                "ProprietaryWorkId", "ISWC", "ComposerAuthorName", "ComposerAuthorPartyId", "ArrangerName",
                "ArrangerPartyId", "MusicPublisherName", "MusicPublisherPartyId", "WorkContributorName",
                "WorkContributorPartyId", "DspReleaseId", "ProprietaryReleaseId", "ReleaseCatalogNumber", "ICPN",
                "ReleaseDisplayArtistName", "ReleaseDisplayArtistPartyId", "ReleaseTitle", "ReleaseSubTitle",
                "ReleaseType", "ReleaseLabelName", "PLine", "ReleaseDataProviderName", "SalesTransactionId",
                "IsRoyaltyBearing", "NumberOfStreams", "PromotionalActivity", "ReleaseDate", "UseType",
                "PriceConsumerPaidExcSalesTax"],  # SRB Record Type for the Basic Audio Profile for Streaming Models
    "SR03.01": ["RecordType", "SummaryRecordId", "DspResourceId", "ISRC", "ResourceTitle", "ResourceSubTitle",
                "ResourceDisplayArtistName", "ResourceDisplayArtistPartyId", "Duration", "ResourceType",
                "MusicalWorkTitle", "DspWorkId", "ISWC", "ComposerAuthorName", "ComposerAuthorPartyId", "ArrangerName",
                "ArrangerPartyId", "MusicPublisherName", "MusicPublisherPartyId", "WorkContributorName",
                "WorkContributorPartyId", "DspReleaseId", "ProprietaryReleaseId", "ReleaseCatalogNumber", "ICPN",
                "ReleaseDisplayArtistName", "ReleaseDisplayArtistPartyId", "ReleaseTitle", "ReleaseSubTitle",
                "ReleaseLabelName", "PLine", "SalesTransactionId", "Usages", "NetRevenue", "ValidityPeriodStart",
                "ValidityPeriodEnd", "ContentCategory", "RightsControllerName", "RightsControllerPartyId",
                "RightsControllerWorkId", "RightShare", "RightsType", "AllocatedNetRevenue", "AllocatedAmount",
                "AllocatedUsages", "Deprecated Cell"],  # Basic SRB Record Type for the UGC Profile
    "SR04.01": ["RecordType", "SummaryRecordId", "DspResourceId", "ISAN", "EIDR", "ProprietaryResourceId", "VideoType",
                "ResourceTitle", "ResourceSubTitle", "ResourceOriginalTitle", "EpisodeNumber", "SeasonNumber", "Genre",
                "Duration", "ResourceDisplayArtistName", "ResourceDisplayArtistPartyId", "ProducerName",
                "ProducerPartyId", "DirectorName", "DirectorPartyId", "ActorName", "ActorPartyId",
                "ProductionCompanyName", "ProductionCompanyPartyId", "LanguageLocalizationType", "HasCaptioning",
                "HasAudioDescription", "OriginalLanguageOfPerformance", "LanguageOfDubbing",
                "DateOfProductionOrRelease", "CountryOfProduction", "OriginalBroadcastChannel",
                "OriginalBroadcastDateTime", "DspReleaseId", "ProprietaryReleaseId", "ICPN", "ReleaseTitle",
                "ReleaseSubTile", "SeriesTitle", "ReleaseType", "DataProviderName", "VideoCategory",
                "SalesTransactionId", "IsDrmEnforced", "VideoDefinitionType", "CodingType", "BitRate",
                "IsRoyaltyBearing", "Downloads", "Returns", "PriceConsumerPaidExcSalesTax", "PromotionalActivity",
                "CueSheetDataProvider", "UseType"],  # SRB Record Type for the Audio-visual Profile for Download Models
    "SR05.01": ["RecordType", "SummaryRecordId", "DspResourceId", "ISAN", "EIDR", "ProprietaryResourceId", "VideoType",
                "ResourceTitle", "ResourceSubTitle", "ResourceOriginalTitle", "EpisodeNumber", "SeasonNumber", "Genre",
                "Duration", "ResourceDisplayArtistName", "ResourceDisplayArtistPartyId", "ProducerName",
                "ProducerPartyId", "DirectorName", "DirectorPartyId", "ActorName", "ActorPartyId",
                "ProductionCompanyName", "ProductionCompanyPartyId", "LanguageLocalizationType", "HasCaptioning",
                "HasAudioDescription", "OriginalLanguageOfPerformance", "LanguageOfDubbing",
                "DateOfProductionOrRelease", "CountryOfProduction", "OriginalBroadcastChannel",
                "OriginalBroadcastDateTime", "DspReleaseId", "ProprietaryReleaseId", "ICPN", "ReleaseTitle",
                "ReleaseSubTile", "SeriesTitle", "ReleaseType", "DataProviderName", "VideoCategory",
                "SalesTransactionId", "VideoDefinitionType", "CodingType", "BitRate", "IsRoyaltyBearing",
                "NumberOfStreams", "PromotionalActivity", "CueSheetDataProvider", "UseType",
                "PriceConsumerPaidExcSalesTax"],  # SRB Record Type for the Audio-visual Profile for Streaming Models
    "SR06.01": ["RecordType", "SummaryRecordId", "DspResourceId", "ISRC", "ResourceTitle", "ResourceSubTitle",
                "ResourceDisplayArtistName", "ResourceDisplayArtistPartyId", "MusicalWorkTitle", "DspWorkId", "ISWC",
                "ComposerAuthorName", "ComposerAuthorPartyId", "Usages", "ValidityPeriodStart", "ValidityPeriodEnd",
                "ContentCategory", "RightsControllerName", "RightsControllerPartyId", "RightsControllerWorkId",
                "RightShare", "RightsType", "AllocatedAmount", "AllocatedNetUsage", "AllocatedNetRevenue"],
    # SRB Record Type for the UGC Profile for Ad-supported and Streaming Models
    "SR07.01": ["RecordType", "BlockId", "SummaryRecordId", "DspReleaseId", "ProprietaryReleaseId",
                "ReleaseCatalogNumber", "ICPN", "ReleaseDisplayArtistName", "ReleaseDisplayArtistPartyId",
                "ReleaseTitle", "ReleaseSubTitle", "ReleaseType", "ReleaseLabelName", "ReleasePLine", "DspResourceId",
                "ISRC", "ResourceTitle", "ResourceSubTitle", "ResourceDisplayArtistName",
                "ResourceDisplayArtistPartyId", "ResourceDuration", "ResourceType", "DspWorkId", "ISWC",
                "MusicalWorkTitle", "MusicalWorkSubTitle", "ComposerAuthorName", "ComposerAuthorPartyId",
                "ArrangerName", "ArrangerPartyId", "MusicPublisherName", "MusicPublisherPartyId", "WorkContributorName",
                "WorkContributorPartyId", "DataProviderName", "ProprietaryWorkId", "UsageForPrioritisation",
                "PercentileForPrioritisation", "UnclaimedPercentage", "NumberOfTransactedResources", "ReleaseDate"],
    # Single Record Block Record for the Masterlist Profile
    "SR08.01": ["RecordType", "SalesTransactionId", "GRid", "ICPN", "DspReleaseId", "LabelReleaseId",
                "ProprietaryReleaseId", "ContextReleaseGRid", "ReleaseType", "ReleaseTitle", "ReleaseSubTitle",
                "ReleaseDisplayArtistName", "ReleaseDisplayArtistPartyId", "ISRC", "ISAN", "DspResourceId",
                "LabelResourceId", "ProprietaryResourceId", "ContextReleaseGRid", "ResourceType", "ResourceTitle",
                "ResourceSubTitle", "ResourceDisplayArtistName", "ResourceDisplayArtistPartyId", "SummaryRecordId",
                "SalesTransactionDate", "Usages", "Returns", "NetUsage", "WholesalePriceInCurrencyOfTransaction",
                "WholesalePriceInCurrencyOfAccounting", "SuggestedConsumerPriceInCurrencyOfTransaction",
                "SuggestedConsumerPriceInCurrencyOfAccounting", "PriceType", "PriceRangeType",
                "PriceConsumerPaidExcSalesTaxInCurrencyOfTransaction",
                "PriceConsumerPaidExcSalesTaxInCurrencyOfAccounting", "DeductionType",
                "DeductionsInCurrencyOfTransaction", "DeductionsInCurrencyOfAccounting", "RightSharePercentage",
                "CalculatedUnitPriceInCurrencyOfTransaction", "CalculatedUnitPriceInCurrencyOfAccounting",
                "AllocatedRevenueInCurrencyOfTransaction", "AllocatedRevenueInCurrencyOfAccounting",
                "AllocatedNetRevenueInCurrencyOfTransaction", "AllocatedNetRevenueInCurrencyOfAccounting",
                "CopyrightObligationWithDSP"],
    # Single Record Block Record Type for Financial Reporting to Record Companies
}

RELEASES = ["RE04"]
RESOURCE_RECORDS = ["AS05", "AS06"]
SALES_USAGES = ["SU01.02", "SU02.02"]
COMPOSITION_RECORDS = ["AS06", "MW02"]