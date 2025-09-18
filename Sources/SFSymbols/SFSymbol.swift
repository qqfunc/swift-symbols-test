public struct SFSymbol {

    init(name: String) { self.name = name }

    /// The name of the symbol.
    public let name: String

}

extension SFSymbol: Hashable {}

extension SFSymbol: Codable {}

extension SFSymbol: Sendable {}
